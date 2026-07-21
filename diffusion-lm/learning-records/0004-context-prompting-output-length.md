# 0004 — Context, prompting, and output length in diffusion LMs

The user asked three practical questions after Lesson 0002 that needed a dedicated bridge note.

**Key clarifications documented:**
- Output length: pure diffusion requires fixed-length canvas upfront; block-autoregressive (DiffusionGemma) is the main workaround
- Prompting: fully supported via conditioning; bidirectional attention is actually better than AR's causal attention for prompt understanding
- Context window: same techniques apply (RoPE, Flash Attention), but diffusion pays attention cost per step × number of steps, making long-context more expensive for transformer-backbone diffusion models
- DiffuMamba's SSM backbone (O(L) vs O(L²)) makes it strategically important for long-context diffusion

**The bridge note** (0002b-context-prompting-output-length.html) links between Lesson 0002 and 0003, serving as a practical reference for when the user builds experiments.
