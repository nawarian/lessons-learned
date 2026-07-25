# Lesson Plan: Diffusion Language Models (v2)

## The Arc (7 lessons theory + 1+ build lessons)

### Phase 1: Foundations (0001-0007) ✅ Complete

| # | Lesson | What You'll Walk Away With |
|---|--------|---------------------------|
| **0001** | **🧪 Feasibility Check: Economics & Hardware Reality** | Straight answers: data needed, training cost, inference behavior on your L40S. Is this worth your time? *You decide whether to continue after this.* |
| **0002** | Why Not Autoregressive? | The structural reason diffusion can beat AR generation |
| **0003** | ✅ Core Mechanics: Forward, Reverse, and the Discrete Problem | How diffusion works, and why text makes it hard |
| **0004** | Masked Diffusion: The Practical Starting Point | The algorithm you can actually implement |
| **0005** | 🧪 Hands-On: Train a Tiny Diffusion LM | A working model on your 8 GB GPU |
| **0006** | 🔭 At Scale: Engineering Anatomy to Fine-Tuning | Layer-by-layer anatomy of your tiny MDLM → how it scales to DiffusionGemma (26B, MoE, block-AR) → DiffuMamba (SSM backbone) → 4 concrete fine-tuning recipes for L40S (QLoRA, LoRA, distillation, multi-node FSDP) |
| **0007** | **📐 Scaling Laws & Your Build Decision** | Synthesis: SMDM 16× compute gap, Chinchilla for diffusion, three viable paths (fine-tune, scratch, distill), concrete build/wait verdict for L40S with Magalu Cloud pricing in R$ |

### Phase 2: Build (0008+) 🚧 In Progress

| # | Lesson | What You'll Walk Away With |
|---|--------|---------------------------|
| **0008** | **🔨 Build: Distill a 300M MDLM from LLaDA 8B** | Complete pipeline: data collection → tokenizer training → teacher setup → distillation training → evaluation. A working 300M Portuguese+English+Agentic coding diffusion LM you can run on your local GPU. |

## How 0001 and 0007 differ

- **0001** is your *pre-feasibility check* — high-level hard numbers to decide if investing learning time makes sense. Approximate, honest, "no bullshit."
- **0007** is your *build decision* — after understanding architectures and training your own tiny model, you get the scaling laws, cost estimates in R$, and a clear build/wait verdict for your L40S.
