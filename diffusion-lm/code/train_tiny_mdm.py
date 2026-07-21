"""
train_tiny_mdm.py — Train a Tiny Masked Diffusion Language Model

Trains a character-level masked diffusion LM on tiny Shakespeare.
Runs on any GPU with ~2 GB VRAM (or CPU, ~15 min).
Based on the MDLM algorithm (Sahoo et al., NeurIPS 2024).

Usage:
    python train_tiny_mdm.py              # train from scratch
    python train_tiny_mdm.py --infer      # generate with saved model
    python train_tiny_mdm.py --steps 1000 # fewer steps for quick demo

Lesson 0005 — Hands-On: Train a Tiny Diffusion LM
"""

import os, sys, math, time, pickle
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

# ─── Configuration ───
class Config:
    # Model
    vocab_size: int = 64       # chars + [MASK] + [PAD] + [BOS]
    d_model: int = 128
    n_layers: int = 4
    n_heads: int = 4
    d_ff: int = 512
    max_seq_len: int = 128
    dropout: float = 0.1

    # Training
    batch_size: int = 64
    lr: float = 3e-4
    weight_decay: float = 0.01
    warmup_steps: int = 100
    train_steps: int = 3000
    log_every: int = 100
    eval_every: int = 500
    device: str = "cuda" if torch.cuda.is_available() else "cpu"

    # Diffusion
    mask_token_id: int = 0     # [MASK] gets index 0
    pad_token_id: int = 1      # [PAD] gets index 1
    num_inference_steps: int = 64
    inference_temp: float = 0.8

    # Paths
    data_url: str = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    data_file: str = os.path.join(os.path.dirname(__file__), "tinyshakespeare.txt")
    save_dir: str = os.path.join(os.path.dirname(__file__), "checkpoints")


# ─── Cosine Masking Schedule ───
def cosine_mask_schedule(t: torch.Tensor) -> torch.Tensor:
    """t in [0, 1], returns masked fraction α(t) ∈ [0, 1]"""
    return 1 - torch.cos((math.pi / 2) * t)


def get_mask(schedule_fn, t: torch.Tensor, seq_len: int) -> torch.BoolTensor:
    """Sample a binary mask for a batch given noise level t ∈ [0, 1]."""
    # t: [B] — noise level per sample in batch
    alpha = schedule_fn(t)  # [B] — fraction to mask per sample
    # Each sample gets alpha_i * seq_len masked tokens (rounded)
    n_mask = (alpha * seq_len).long().clamp(1, seq_len - 1)
    B = t.shape[0]
    mask = torch.zeros(B, seq_len, dtype=torch.bool, device=t.device)
    for i in range(B):
        perm = torch.randperm(seq_len, device=t.device)
        mask[i, perm[:n_mask[i]]] = True
    return mask


# ─── Dataset ───
class CharDataset(Dataset):
    """Character-level dataset: encode text as token IDs."""

    def __init__(self, text: str, seq_len: int):
        self.seq_len = seq_len
        # Build vocab from characters in text
        chars = sorted(set(text))
        # Reserve 0 for [MASK], 1 for [PAD], 2 for [BOS] (if needed)
        self.stoi = {ch: i + 3 for i, ch in enumerate(chars)}
        self.itos = {i + 3: ch for i, ch in enumerate(chars)}
        self.itos[0] = '[MASK]'
        self.itos[1] = '[PAD]'
        self.itos[2] = '[BOS]'
        self.vocab_size = len(chars) + 3

        # Tokenize entire text
        self.data = torch.tensor([self.stoi.get(c, 1) for c in text], dtype=torch.long)
        self.num_samples = max(1, (len(self.data) - seq_len) // seq_len)

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        start = idx * self.seq_len
        end = start + self.seq_len
        chunk = self.data[start:end]
        if len(chunk) < self.seq_len:
            chunk = F.pad(chunk, (0, self.seq_len - len(chunk)), value=1)
        return chunk


# ─── Transformer Backbone ───
class SinusoidalEmbedding(nn.Module):
    """Sinusoidal time embedding used in diffusion models."""
    def __init__(self, d_model: int, max_period: int = 10000):
        super().__init__()
        self.d_model = d_model
        self.max_period = max_period

    def forward(self, t: torch.Tensor) -> torch.Tensor:
        # t: [B] — noise levels in [0, 1]
        device = t.device
        half = self.d_model // 2
        freqs = torch.exp(-math.log(self.max_period) * torch.arange(half, device=device) / half)
        args = t.unsqueeze(-1) * freqs.unsqueeze(0)  # [B, half]
        emb = torch.cat([torch.cos(args), torch.sin(args)], dim=-1)  # [B, d_model]
        return emb


class MDMBackbone(nn.Module):
    """
    A small bidirectional transformer for masked diffusion.
    Takes token IDs + noise level → logits over vocabulary.
    """
    def __init__(self, cfg: Config):
        super().__init__()
        self.cfg = cfg

        self.token_embed = nn.Embedding(cfg.vocab_size, cfg.d_model)
        self.pos_embed = nn.Embedding(cfg.max_seq_len, cfg.d_model)
        self.time_embed = nn.Sequential(
            SinusoidalEmbedding(cfg.d_model),
            nn.Linear(cfg.d_model, cfg.d_model),
            nn.GELU(),
            nn.Linear(cfg.d_model, cfg.d_model),
        )
        self.time_scale = nn.Linear(cfg.d_model, cfg.d_model)
        self.time_shift = nn.Linear(cfg.d_model, cfg.d_model)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=cfg.d_model,
            nhead=cfg.n_heads,
            dim_feedforward=cfg.d_ff,
            dropout=cfg.dropout,
            activation='gelu',
            batch_first=True,
            norm_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=cfg.n_layers)

        self.norm = nn.LayerNorm(cfg.d_model)
        self.head = nn.Linear(cfg.d_model, cfg.vocab_size)

        # Initialize weights
        self.apply(self._init_weights)

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
        elif isinstance(module, nn.LayerNorm):
            torch.nn.init.zeros_(module.bias)
            torch.nn.init.ones_(module.weight)

    def forward(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [B, L] token IDs (with [MASK]=0 for masked positions)
            t: [B] noise levels in [0, 1]
        Returns:
            logits: [B, L, V]
        """
        B, L = x.shape
        device = x.device

        # Token embeddings
        tok_emb = self.token_embed(x)  # [B, L, d]

        # Position embeddings
        positions = torch.arange(L, device=device).unsqueeze(0)  # [1, L]
        pos_emb = self.pos_embed(positions)  # [1, L, d]

        # Time embedding (broadcast to all positions)
        t_emb = self.time_embed(t)  # [B, d]
        t_scale = self.time_scale(t_emb).unsqueeze(1)  # [B, 1, d]
        t_shift = self.time_shift(t_emb).unsqueeze(1)  # [B, 1, d]

        # Modulate token embeddings with time
        h = tok_emb * (1 + t_scale) + t_shift
        h = h + pos_emb

        # Pass through transformer (bidirectional — no causal mask)
        h = self.transformer(h)  # [B, L, d]

        # Project to vocabulary
        h = self.norm(h)
        logits = self.head(h)  # [B, L, V]

        return logits


# ─── Diffusion Process ───
def cosine_fn(t):
    return 1 - torch.cos((math.pi / 2) * t)


def forward_process(x0: torch.Tensor, t: torch.Tensor,
                    mask_token_id: int, schedule_fn=cosine_fn) -> tuple:
    """
    Corrupt clean tokens with masking.
    Args:
        x0: [B, L] clean token IDs
        t: [B] noise levels in [0, 1]
    Returns:
        x_t: [B, L] corrupted tokens
        mask: [B, L] boolean mask of masked positions
    """
    B, L = x0.shape
    device = x0.device
    alpha = schedule_fn(t)  # [B] fraction to mask per sample
    n_mask = (alpha * L).long().clamp(1, L - 1)

    mask = torch.zeros(B, L, dtype=torch.bool, device=device)
    for i in range(B):
        perm = torch.randperm(L, device=device)
        mask[i, perm[:n_mask[i]]] = True

    x_t = x0.clone()
    x_t[mask] = mask_token_id
    return x_t, mask


def train_step(model, optimizer, x0, mask_token_id, schedule_fn=cosine_fn):
    """Single training step for masked diffusion."""
    B, L = x0.shape
    device = x0.device

    # Sample noise level uniformly per sample
    t = torch.rand(B, device=device)  # [B] uniform in [0, 1]

    # Forward process: corrupt x0
    x_t, mask = forward_process(x0, t, mask_token_id, schedule_fn)

    # Predict logits for all positions
    logits = model(x_t, t)  # [B, L, V]

    # Loss on masked positions only
    logits_masked = logits[mask]  # [N_masked, V]
    targets_masked = x0[mask]  # [N_masked]
    loss = F.cross_entropy(logits_masked, targets_masked)

    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()

    return loss.item()


@torch.no_grad()
def generate(model, cfg: Config, prompt: Optional[str] = None,
             prompt_dataset=None, num_steps: Optional[int] = None,
             temperature: float = 0.8) -> list[int]:
    """
    Generate text using iterative masked diffusion.
    
    If prompt is given, tokens up to len(prompt) are treated as fixed context.
    Otherwise, generates from scratch (all masked).
    """
    model.eval()
    device = next(model.parameters()).device
    L = cfg.max_seq_len
    if num_steps is None:
        num_steps = cfg.num_inference_steps

    # Initialize: fully masked (or partially from prompt)
    tokens = torch.full((1, L), cfg.mask_token_id, dtype=torch.long, device=device)

    if prompt is not None and prompt_dataset is not None:
        # Encode prompt
        prompt_ids = []
        for ch in prompt:
            if ch in prompt_dataset.stoi:
                prompt_ids.append(prompt_dataset.stoi[ch])
            else:
                prompt_ids.append(prompt_dataset.stoi.get(' ', 3))  # fallback to space
        prompt_len = min(len(prompt_ids), L)
        tokens[0, :prompt_len] = torch.tensor(prompt_ids[:prompt_len], device=device)

    for step in range(num_steps):
        # Current noise level (going from 1 → 0)
        t_val = 1.0 - (step / num_steps)
        t_next = 1.0 - ((step + 1) / num_steps)
        t = torch.full((1,), t_val, device=device)

        # Forward pass
        logits = model(tokens, t)  # [1, L, V]

        # Sample from logits with temperature
        probs = F.softmax(logits / temperature, dim=-1)  # [1, L, V]

        # For fixed prompt positions, keep them (skip sampling)
        if prompt is not None and prompt_dataset is not None:
            prompt_len = min(len(prompt), L)
            fixed_mask = torch.zeros(1, L, dtype=torch.bool, device=device)
            fixed_mask[0, :prompt_len] = (tokens[0, :prompt_len] != cfg.mask_token_id)
        else:
            fixed_mask = torch.zeros(1, L, dtype=torch.bool, device=device)

        # Sample tokens
        sampled = torch.multinomial(probs.view(-1, cfg.vocab_size), num_samples=1).view(1, L)

        # Determine which masked positions to reveal this step
        alpha_now = cosine_fn(torch.tensor([t_val], device=device))
        alpha_next = cosine_fn(torch.tensor([t_next], device=device))
        n_to_reveal = max(1, int((alpha_now - alpha_next).item() * L))

        # Find still-masked positions (excluding fixed prompt)
        is_masked = (tokens == cfg.mask_token_id) & ~fixed_mask  # [1, L]
        masked_indices = is_masked[0].nonzero(as_tuple=True)[0]

        if len(masked_indices) == 0:
            break

        # Get confidence scores for masked positions
        confidences = probs[0, masked_indices].max(dim=-1).values  # [N_masked]

        # Reveal the n_to_reveal highest-confidence positions
        n_reveal = min(n_to_reveal, len(masked_indices))
        top_conf_idx = confidences.topk(n_reveal).indices  # indices into masked_indices
        reveal_positions = masked_indices[top_conf_idx]

        # Update tokens at revealed positions
        tokens[0, reveal_positions] = sampled[0, reveal_positions]

    # Final pass: fill any remaining masked positions with argmax
    final_logits = model(tokens, torch.tensor([0.0], device=device))
    final_probs = F.softmax(final_logits / temperature, dim=-1)
    final_tokens = final_probs.argmax(dim=-1)
    remaining_mask = (tokens == cfg.mask_token_id)
    tokens[remaining_mask] = final_tokens[remaining_mask]

    return tokens[0].tolist()


# ─── Data Loading ───
def download_shakespeare(cfg: Config) -> str:
    """Download tiny Shakespeare if not already present."""
    if os.path.exists(cfg.data_file):
        with open(cfg.data_file, 'r') as f:
            return f.read()

    print(f"Downloading tiny Shakespeare from {cfg.data_url}...")
    import urllib.request
    urllib.request.urlretrieve(cfg.data_url, cfg.data_file)
    with open(cfg.data_file, 'r') as f:
        return f.read()

    return text


# ─── Training Loop ───
def train(cfg: Config):
    print(f"Device: {cfg.device}")
    print(f"Training steps: {cfg.train_steps}")

    # Data
    text = download_shakespeare(cfg)
    dataset = CharDataset(text, cfg.max_seq_len)
    cfg.vocab_size = dataset.vocab_size  # update with actual vocab size
    print(f"Vocab size: {cfg.vocab_size} ({cfg.vocab_size - 3} characters + [MASK], [PAD], [BOS])")
    print(f"Dataset: {len(dataset)} samples ({len(text):,} chars)")

    dataloader = DataLoader(
        dataset, batch_size=cfg.batch_size, shuffle=True,
        num_workers=0, pin_memory=(cfg.device == 'cuda'),
        drop_last=True
    )

    # Model
    model = MDMBackbone(cfg).to(cfg.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model parameters: {n_params:,}")
    print(f"Model size: {n_params * 4 / 1024 / 1024:.2f} MB (FP32)")

    # Optimizer
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=cfg.lr,
        weight_decay=cfg.weight_decay,
        betas=(0.9, 0.999),
    )

    # Learning rate scheduler with linear warmup
    def lr_lambda(step):
        if step < cfg.warmup_steps:
            return step / max(1, cfg.warmup_steps)
        return 1.0

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    # Training
    os.makedirs(cfg.save_dir, exist_ok=True)
    model.train()
    step = 0
    best_loss = float('inf')
    train_iter = iter(dataloader)

    print(f"\n{'Step':>6} | {'Loss':>8} | {'Time':>8}")
    print('-' * 30)

    start_time = time.time()
    while step < cfg.train_steps:
        try:
            batch = next(train_iter)
        except StopIteration:
            train_iter = iter(dataloader)
            batch = next(train_iter)

        x0 = batch.to(cfg.device)

        loss = train_step(model, optimizer, x0, cfg.mask_token_id, cosine_fn)
        scheduler.step()
        step += 1

        if step % cfg.log_every == 0:
            elapsed = time.time() - start_time
            print(f"{step:>6} | {loss:>8.4f} | {elapsed:>7.1f}s")
            best_loss = min(best_loss, loss)

    total_time = time.time() - start_time
    print(f"\n✅ Training complete in {total_time:.1f}s ({total_time/60:.1f} min)")
    print(f"Best loss: {best_loss:.4f}")

    # Save model
    save_path = os.path.join(cfg.save_dir, "tiny_mdm.pt")
    torch.save({
        'model_state_dict': model.state_dict(),
        'cfg': cfg,
        'stoi': dataset.stoi,
        'itos': dataset.itos,
        'vocab_size': cfg.vocab_size,
    }, save_path)
    print(f"Model saved to {save_path}")

    return model, dataset


@torch.no_grad()
def demo_generation(model, dataset, cfg: Config, prompt: str = ""):
    """Generate text and print it."""
    tokens = generate(model, cfg, prompt=prompt if prompt else None,
                      prompt_dataset=dataset if prompt else None,
                      temperature=cfg.inference_temp)

    # Decode
    generated = ''.join([dataset.itos.get(t, '?') for t in tokens])
    # Strip special tokens
    generated = generated.replace('[MASK]', '').replace('[PAD]', '').replace('[BOS]', '')
    # Remove repeated spaces
    while '  ' in generated:
        generated = generated.replace('  ', ' ')

    print(f"\nPrompt: \"{prompt}\"")
    print(f"Generated ({len(tokens)} tokens):")
    print('─' * 50)
    print(generated)
    print('─' * 50)
    return generated


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Train a tiny Masked Diffusion Language Model")
    parser.add_argument('--steps', type=int, default=None, help='Training steps')
    parser.add_argument('--infer', action='store_true', help='Generate with saved model instead of training')
    parser.add_argument('--prompt', type=str, default='', help='Prompt for generation')
    parser.add_argument('--temp', type=float, default=None, help='Sampling temperature')
    parser.add_argument('--batch-size', type=int, default=None, help='Batch size')
    args = parser.parse_args()

    cfg = Config()
    if args.steps:
        cfg.train_steps = args.steps
    if args.batch_size:
        cfg.batch_size = args.batch_size
    if args.temp:
        cfg.inference_temp = args.temp

    if args.infer:
        # Load saved model
        save_path = os.path.join(cfg.save_dir, "tiny_mdm.pt")
        if not os.path.exists(save_path):
            print(f"No saved model found at {save_path}. Train first with no arguments.")
            return

        checkpoint = torch.load(save_path, map_location=cfg.device, weights_only=False)
        saved_cfg = checkpoint['cfg']
        cfg.vocab_size = checkpoint['vocab_size']

        # Reconstruct dataset info for decoding
        class DatasetStub:
            pass
        dataset = DatasetStub()
        dataset.stoi = checkpoint['stoi']
        dataset.itos = checkpoint['itos']
        dataset.vocab_size = cfg.vocab_size

        model = MDMBackbone(cfg).to(cfg.device)
        model.load_state_dict(checkpoint['model_state_dict'])
        model.eval()
        print(f"Loaded model from {save_path}")

        demo_generation(model, dataset, cfg, prompt=args.prompt)
    else:
        model, dataset = train(cfg)
        print("\n" + "=" * 50)
        print("Generating samples...")
        print("=" * 50)

        # Generate without prompt
        demo_generation(model, dataset, cfg, prompt="")

        # Generate with a short prompt
        if len(args.prompt) > 0:
            demo_generation(model, dataset, cfg, prompt=args.prompt)


if __name__ == '__main__':
    main()
