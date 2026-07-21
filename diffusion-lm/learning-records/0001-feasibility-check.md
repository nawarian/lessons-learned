# 0001 — Feasibility check established: diffusion LMs are viable for single-GPU experimentation, not for SOTA training

The user's hardware constraints were defined: 8 GB VRAM local, 48 GB L40S cloud. The key numbers from SMDM, LLaDA, SEDD, and MDLM papers were compiled into a feasibility assessment.

**Key findings:**
- Training from scratch: ≤100M on 8 GB, ≤1B on L40S (with gradient accumulation)
- Inference: LLaDA 8B (4-bit) fits on 8 GB local; LLaDA 8B (BF16) and DiffusionGemma (4-bit) fit on L40S
- Diffusion LMs need 16× more training compute than ARMs (per SMDM), but inference is 1.4× faster and tunable
- LLaDA 8B cost 130K H800 GPU-hours — not reproducible on single GPU
- DiffuMamba code has not been publicly released

**Implications:** The user should focus on understanding masked diffusion (MDLM) as the most practical accessible approach, building small models for intuition, and using existing large models (LLaDA) for inference experiments. The field is early enough that expertise built now will be valuable.
