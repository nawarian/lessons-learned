# 0008 — Lesson 0005 built: Hands-On — Train a Tiny Diffusion LM

Lesson 0005 was delivered. A full hands-on session with training code and interactive lesson page.

**Deliverables:**
- `lessons/0005-train-tiny-diffusion-lm.html` — Lesson page with step-by-step code walkthrough, terminal output examples, experiment suggestions, checklist, and 4 comprehension quizzes
- `code/train_tiny_mdm.py` — Standalone self-contained Python script (~250 lines) implementing a character-level masked diffusion LM from scratch

**Model architecture:**
- 2.5M parameter bidirectional transformer encoder
- 4 layers, 4 heads, 128-dim embeddings, 512-dim FFN
- Character-level tokenizer (~60 vocab including [MASK] and [PAD])
- 128 character sequence length
- Time conditioning via sinusoidal embedding → scale/shift modulation (adaLN)
- Cosine masking schedule (same as MDLM/LLaDA)

**Training details:**
- Dataset: Tiny Shakespeare (~200K chars, downloaded automatically)
- Objective: Cross-entropy on masked positions only (standard MLM loss)
- 3000 steps, batch size 64, AdamW lr=3e-4 with linear warmup
- ~5 min on CUDA GPU, ~15 min on CPU
- ~1.5 GB VRAM required

**Inference details:**
- Iterative confidence-based denoising from all-masked state
- Configurable steps (default 64) and temperature (default 0.8)
- Supports prompting (fixed prefix tokens)

**Key teaching points:**
- Step-by-step code walkthrough (config → schedule → tokenizer → model → training → inference)
- The training algorithm in 4 lines: sample noise → mask → predict → cross-entropy on masked positions
- Why the noise level t is needed as input (adaLN conditioning)
- How confidence-based unmasking works as the "reveal smart, not random" strategy
- Why single-step inference = BERT (one pass, all masks filled at once)
- L40S upgrade path: BPE tokenizer, deeper model, longer sequences, Portuguese text

**User interaction:** Can run the training script immediately. Expected to try temperature variations, step counts, and model depth experiments.

**Implication:** Ready for Lesson 0006 (Diffusion at scale — DiffusionGemma, DiffuMamba, scaling laws).
