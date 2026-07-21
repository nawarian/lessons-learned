# 0007 — Lesson 0004 built: Masked Diffusion — The Practical Starting Point

Lesson 0004 was delivered. Covers the masked diffusion algorithm in depth — the practical approach the user will implement in Lesson 0005.

**Key content:**
- Why masked diffusion wins on simplicity: cross-entropy loss, no transition matrices, ~50 lines on top of a transformer
- Forward process: gradual token replacement with [MASK] according to a schedule (cosine > uniform)
- Interactive forward masking simulation with the sentence "O rato roeu a roupa do rei de Roma."
- Masking schedule comparison (cosine, uniform, γ) with interactive canvas plot
- Reverse process: starting from all-masked, iteratively reveal highest-confidence predictions
- Interactive denoising simulation showing tokens revealed step by step
- Full training and inference pseudo-code in a clean algorithm card
- Training vs inference cost comparison table (masked diffusion vs AR)
- Clarification: how masked diffusion differs from BERT (same training objective, different inference procedure)
- MDLM derivation light (mixture of MLM losses, weighting functions)
- LLaDA 8B as a pre-trained model that runs on the user's L40S today

**Interactive elements:**
1. Forward masking slider — watch tokens get [MASK]ed progressively
2. Schedule comparison canvas — 4 schedules overlaid with toggle buttons
3. Denoising simulation — step-by-step iterative unmasking with configurable steps/speed
4. Revelation schedule explorer — watch the schedule in action revealing tokens
5. Quiz (4 questions: 3 single-select, 1 multi-select)

**User interaction:** Interactive lesson with multiple visual simulations and comprehension quizzes.

**Hardware notes included:**
- L40S can train ~350M param masked diffusion on 512-length sequences with batch 16-32
- LLaDA 8B fits on L40S with 4-bit quantization (~5 GB VRAM)
- Training cost ~2× an AR model for same perplexity (more steps needed)

**Implication:** Ready for Lesson 0005 (hands-on training of a tiny diffusion LM on the user's GPU).
