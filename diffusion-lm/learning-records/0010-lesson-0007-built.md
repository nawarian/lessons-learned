# 0010 — Lesson 0007 built: Scaling Laws & Build Decision

Lesson 0007 was delivered — the final synthesis lesson completing the 7-lesson arc on diffusion language models.

**Key content:**
- **Part 1 (Scaling Laws):** SMDM 16× compute gap explained. Iso-FLOP contour visualization (1B MDLM = 125M AR quality). Chinchilla applied to diffusion — a 300M MDLM has ~19M AR quality ceiling on general text.
- **Part 2 (Hardware in Perspective):** Real benchmarks from the user's tiny MDLM scaled to L40S. Single L40S (48 GB) vs 4-node cluster (192 GB). Magalu Cloud pricing in R$ for all scenarios. The "R$ 0" insight: existing VM costs R$ 6.310/month regardless, so training on it has zero incremental cost.
- **Part 3 (Three Paths Forward):** Path A — Fine-tune LLaDA 8B with QLoRA (3 hours, R$ 0, full 8B quality). Path B — Train 300M from scratch (1 day, R$ 0-216, full ownership). Path C — Distill LLaDA 8B → 300M student (2-3 days, R$ 0-416, best of both worlds). Each with detailed recipes, cost tables, risk assessments, and scoring.
- **Part 4 (Build Decision):** Decision tree mapping user goals → paths. Timeline comparison (3h vs 1d vs 3d vs 3w). Risk matrix across 5 dimensions. Two verdict banners: **BUILD** (fine-tune existing models or train 300M domain-specialized) and **WAIT** (for 200K context — DiffuMamba isn't ready for production fine-tuning yet).
- **Part 5 (Next Steps):** Concrete week-by-week plan (Week 1: Path A, Week 2: Path B, Week 3: Compare & Deploy).
- **5 comprehension quizzes** covering the compute gap, quality ceilings, fine-tuning economics, 200K context feasibility, and distillation ownership.

**Key insights from this session:**
1. The 16× compute gap is the single most important number for the build decision — it makes training from scratch economically uncompetitive with AR, but fine-tuning bypasses it entirely.
2. "Domain specialization" is the user's edge. A 300M diffusion model trained solely on Portuguese technical docs outperforms its 19M AR equivalent significantly — the scaling laws measure general text loss, not task-specific performance.
3. The "R$ 0" insight is powerful: since the user already pays R$ 6.310/month for the L40S VM, any training that completes within the month is effectively free in terms of cloud costs.
4. Distillation (Path C) is the most interesting long-term strategy but has the highest technical risk due to less-standardized tooling.

**Updated files:**
- `lessons/0007-scaling-laws-build-decision.html` — New lesson built from scratch
- `lessons/0006-at-scale-diffusion-gemma-mamba.html` — Navigation links updated to point to 0007
- `LESSON-PLAN.md` — Updated entry for 0007

**Arc complete:** All 7 lessons (0001-0007) are now built. The user can:
1. Explain how diffusion for text works (forward, reverse, discrete problem)
2. Evaluate a diffusion LM paper and estimate reproduction cost on their hardware
3. Know the numbers — FLOPs, memory, training time for reference implementations
4. Train a tiny diffusion LM from scratch
5. Fine-tune production-scale diffusion LMs on their L40S
6. Make an informed build-or-wait decision
