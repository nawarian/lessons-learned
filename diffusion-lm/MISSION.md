# Mission: Diffusion-based Language Models

## Why
I want to understand whether diffusion-based text generation architectures — alternatives to autoregressive transformers — are viable to **build and train myself** within Brazilian hardware and budget constraints. The goal is to identify a path where I can prototype locally (8 GB VRAM) and scale to a single L40S (48 GB VRAM, 64 GB RAM) for training and inference, without needing clusters of A100s.

## Success looks like
- I can **explain** how diffusion for text works — forward process, reverse process, and the discrete-to-continuous bridge — in my own words
- I can **evaluate** a diffusion LM paper (architecture, cost, results) and estimate whether I could reproduce or adapt it on my hardware
- I **know the numbers** — approximate FLOPs, memory, and training time for DiffusionGemma, DiffuMamba, and reference implementations
- I can **train a tiny diffusion LM** (character-level or small vocab) on my local GPU and see it generate coherent text
- I have a **concrete assessment** of whether building a diffusion LM at meaningful scale is realistic for my L40S, or whether the field is still too expensive for single-GPU practitioners

## Constraints
- **Hardware ceiling** (local): 8 GB VRAM GPU (prototyping, small-scale experiments)
- **Hardware ceiling** (cloud): 1× L40S (48 GB VRAM), 64 GB RAM, 8 vCPUs, expandable SSD (~100 GB+)
- **Time**: days to weeks for the learning arc
- **Learning style**: hands-on with code where possible, but need enough theoretical intuition to read papers and make architectural decisions
- **Budget**: training on L40S is fine for small-to-medium runs; renting A100 clusters is not viable

## Out of scope
- Becoming a researcher who designs novel architectures from scratch
- Comprehensive survey of every diffusion LM paper published
- Deep dive into the mathematical proofs of score matching, ELBO derivations, or SDE/ODE formulations
- Image diffusion models (stable diffusion, etc.) except as analogies to build intuition
