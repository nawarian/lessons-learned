# 0009 — Lesson 0006 built: Engineering Anatomy to Fine-Tuning

Lesson 0006 was delivered — a significant expansion from the original lesson plan. The user expressed that although they can run and tweak the architecture, they cannot yet "see" what each layer does internally. This lesson addressed that gap directly.

**Key content:**
- **Part 1 (Engineering Anatomy):** Layer-by-layer breakdown of the user's tiny MDLM — token embedding (lookup table, vocab scaling), position embedding (learned vs RoPE), time embedding (sinusoidal → adaLN scale/shift), self-attention (the "diffusion" engine, O(L²) cost), FFN (knowledge storage, per-position "thinking"), residual connections (gradient flow, diffusion-specific modulation), and the full per-block signal path. Each section includes parameter counts and fine-tuning implications.
- **Part 2 (DiffusionGemma):** Same building blocks at 10,000× scale. Architecture comparison table (2.5M vs 26B). MoE mechanics (16 experts, top-2 routing, why it changes fine-tuning). Block-autoregressive for variable-length output.
- **Part 3 (DiffuMamba):** Self-attention replaced by SSM. O(L) vs O(L²) scaling. No KV-cache. VRAM implications for 200K context. DiffuMamba code not yet released — recommendation to wait.
- **Part 4 (Fine-Tuning Recipes):** Four concrete recipes ordered by cost:
  1. LLaDA 8B + QLoRA on single L40S (2-4 hours, ~11 GB VRAM) — recommended starting point
  2. DiffusionGemma + LoRA on single L40S with 4-bit quant (~28 GB VRAM, 8-12 hours)
  3. Distillation from LLaDA to custom architecture (2-3 days, full ownership)
  4. Multi-node FSDP on 2× L40S for BF16 LoRA (~23 GB per GPU)

**Decision tree** mapping user goals → recipes. Interactive quizzes (5 questions).

**Implication:** Ready for Lesson 0007 (Scaling Laws & Build Decision) — the final synthesis session.
