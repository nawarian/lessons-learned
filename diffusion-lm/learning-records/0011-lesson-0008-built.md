# 0011 — Lesson 0008 built: Build — Distill a 300M MDLM from LLaDA 8B

Lesson 0008 was delivered — the first "build" lesson in Phase 2, moving from theory to implementation.

**Key content:**
- **Complete pipeline** of 7 numbered scripts from data collection to evaluation
- **Step 1 — Data Collection:** Downloads FineWeb-Edu (EN), CulturaX (PT), The Stack (code), and MaxDevv/real-pi-coding-agent-traces-sessions with proper streaming, filtering, and normalization
- **Step 2 — Tokenizer:** BPE tokenizer (32,768 vocab) trained on mixed corpus with ByteLevel pre-tokenizer for Unicode support. Includes verification test
- **Step 3 — Tokenize & Shard:** Converts raw text to binary .bin shards (uint16 format, ~20 shards × 50M tokens = ~1B tokens, ~2 GB)
- **Step 4 — Student Architecture:** Full 300M MDLM implementation in `config.py` + `model.py`:
  - RoPE position encoding (instead of learned absolute from Lesson 0005)
  - adaLN time conditioning (scale + shift per block)
  - Pre-norm transformer encoder (20 layers, 1024-dim, 16 heads)
  - Cosine noise schedule with confidence-based iterative denoising at inference
  - ~321M parameters
- **Step 5 — Teacher Setup:** LLaDA 8B in 4-bit NF4 quantization (~5 GB VRAM)
- **Step 6 — Distillation Loop:** Full training script with:
  - Shard streaming dataset (loads .bin files, yields random sequences)
  - Adafactor optimizer (saves ~8 bytes/param vs AdamW)
  - Dual loss: KL(student || teacher) + cross-entropy on masked tokens
  - Alpha decay schedule (0.5 → 0 over training)
  - Gradient accumulation, checkpointing, logging
  - Expected ~27 hours on L40S
- **Step 7 — Evaluation:** Three levels: qualitative generation, perplexity, teacher-student agreement
- **Bonus:** Standalone `generate.py` for inference anywhere (including local 8 GB GPU, ~1 GB VRAM)
- **5 comprehension quizzes** covering Adafactor, alpha decay, 4-bit quantization, confidence-based generation, and local GPU feasibility

**Updated files:**
- `lessons/0008-build-distill-300m-mdlm.html` — New lesson built
- `lessons/0006-at-scale-diffusion-gemma-mamba.html` — Navigation added pointing to 0008
- `lessons/0007-scaling-laws-build-decision.html` — Navigation added pointing to 0008
- `LESSON-PLAN.md` — Added Phase 2 with lesson 0008 entry

**Key design decisions:**
1. **Adafactor over AdamW** — saves ~2.6 GB at 321M params, enough to fit teacher + student in VRAM
2. **Alpha decay for distillation** — student learns from teacher early, denoises independently later
3. **Shard-based dataset** — .bin uint16 format avoids JSON parsing overhead during training
4. **Confidence-based token revelation** at inference — same strategy as Lesson 0005's tiny MDLM
5. **All scripts runnable independently** — data prep (steps 1-3) can run on any machine, only distillation needs L40S
