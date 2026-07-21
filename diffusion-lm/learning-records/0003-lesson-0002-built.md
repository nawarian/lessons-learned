# 0003 — Lesson 0002 built: the autoregressive bottleneck

Lesson 0002 was delivered. Covers the structural sequential dependency of AR generation and how diffusion breaks the chain.

**Key content:**
- Interactive simulation comparing AR (token-by-token) vs diffusion (parallel steps) generation
- The cost curve: AR pays O(length) serial passes, diffusion pays fixed N_steps
- KV-cache as a palliative that doesn't solve the serial dependency
- Train-inference mismatch: AR trains in parallel but infers sequentially
- Wall-clock latency vs raw FLOPs: diffusion wins on latency at longer sequences

**User interaction:** User ran the simulation, played with sequence length and diffusion step controls. User confirmed understanding of the sequential bottleneck.

**Implication:** Ready for Lesson 0003 (core mechanics: how forward/reverse diffusion works at the algorithmic level).
