# 0006 — Bridge note: context length management for MDLMs

Built a bridge note (0003b-context-length-management.html) in response to the user's question about how masked diffusion LMs handle long context (e.g., 200K tokens for coding).

**Key content:**
- Why same number of diffusion passes ≠ same VRAM (activations scale O(L × d_model × layers))
- Flash Attention fixes attention score memory but not activation memory or O(L²) FLOPs
- RoPE extrapolation: 4K→8K works, 4K→200K doesn't
- Four levers compared: brute-force pretrain, sliding window, SSM backbone (DiffuMamba), block-AR hybrid
- Practical recommendations: short context (256-512) for lessons 0004-0005, SSM backbone for 200K future, block-AR as current workaround
- Updated lesson plan progression table with context length targets
