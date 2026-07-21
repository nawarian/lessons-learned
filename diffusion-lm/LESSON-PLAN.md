# Lesson Plan: Diffusion Language Models (v2)

## The Arc (7 lessons, ~30 min each)

| # | Lesson | What You'll Walk Away With |
|---|--------|---------------------------|
| **0001** | **🧪 Feasibility Check: Economics & Hardware Reality** | Straight answers: data needed, training cost, inference behavior on your L40S. Is this worth your time? *You decide whether to continue after this.* |
| **0002** | Why Not Autoregressive? | The structural reason diffusion can beat AR generation |
| **0003** | ✅ Core Mechanics: Forward, Reverse, and the Discrete Problem | How diffusion works, and why text makes it hard |
| **0004** | Masked Diffusion: The Practical Starting Point | The algorithm you can actually implement |
| **0005** | 🧪 Hands-On: Train a Tiny Diffusion LM | A working model on your 8 GB GPU |
| **0006** | At Scale: DiffusionGemma & DiffuMamba | What they built, at what cost, on what hardware |
| **0007** | Scaling Laws & Your Build Decision | Synthesis: exactly what you can build on your L40S |

## How 0001 and 0007 differ

- **0001** is your *pre-feasibility check* — high-level hard numbers to decide if investing learning time makes sense. Approximate, honest, "no bullshit."
- **0007** is your *build decision* — after understanding architectures and training your own tiny model, you get precise cost estimates for your specific hardware and use case.
