# 0002 — Vocabulary size & training feasibility on L40S cluster

The user proposed reducing vocabulary size (by pruning languages) as a way to make diffusion LM training more feasible on their 2×L40S-node cluster.

**Key findings from analysis:**
- Embedding/head params can be 30-50% of small models (at 128K vocab), but reducing vocab mostly saves memory, not compute
- The transformer's attention + FFN layers dominate FLOPs (~61% at 1B scale) — the 16× compute gap lives there
- A Portuguese-optimized model (8K vocab, 300M params, 2-5B tokens) would be genuinely trainable on a single L40S in 3-5 days
- This reframed the mission: "build something you own" rather than "compete with Google"
- The user chose to keep existing lesson plan but will use this context when interpreting architectures

**Implications:** Future lessons should reference Portuguese-language applicability and single-GPU feasibility where relevant. Lesson 0004 (hands-on) could prototype with a character-level or small-vocab tokenizer to mirror the Portuguese strategy at a smaller scale.
