# Diffusion Language Models — Resources

Curated high-trust resources for understanding and building diffusion-based text generation models. Updated as knowledge deepens.

## Knowledge

### Foundational Papers

- **MDLM: *Simple and Effective Masked Diffusion Language Models*** — Sahoo et al., NeurIPS 2024
  [arXiv:2406.07524](https://arxiv.org/abs/2406.07524) | [Code (PyTorch)](https://github.com/kuleshov-group/mdlm) | [Project Page](https://s-sahoo.com/mdlm)
  **Best starting point** for discrete diffusion for text. Derives a simple objective (mixture of masked LM losses). Use for: understanding the core masked diffusion algorithm, running small-scale experiments on single GPU.

- **SEDD: *Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution*** — Lou et al., ICML 2024 Best Paper
  [arXiv:2310.16834](https://arxiv.org/abs/2310.16834) | [Code](https://github.com/louaaron/Score-Entropy-Discrete-Diffusion)
  State-of-the-art discrete diffusion theory. Beats GPT-2 perplexity. Use for: deep theoretical grounding, controllable generation, compute-quality tradeoffs.

- **D3PM: *Structured Denoising Diffusion Models in Discrete State-Spaces*** — Austin et al., Google Brain, 2021
  [arXiv:2107.03006](https://arxiv.org/abs/2107.03006)
  Early discrete diffusion paper. Introduces transition matrices for discrete spaces (uniform, absorbing, etc.). Use for: foundations of discrete diffusion, understanding the design space.

- **Diffusion-LM: *Diffusion-LM Improves Controllable Text Generation*** — Li et al., Stanford, NeurIPS 2022
  [arXiv:2205.14217](https://arxiv.org/abs/2205.14217)
  First paper to apply continuous diffusion (Gaussian vectors) to text. Use for: historical context, understanding the continuous→discrete evolution.

### Architecture-Specific Papers

- **DiffusionGemma** — Google DeepMind, 2025
  [Blog Post](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/) | [Documentation](https://ai.google.dev/gemma/docs/diffusiongemma) | [Hugging Face](https://huggingface.co/google/diffusiongemma-26B-A4B-it)
  26B MoE (3.8B active params) diffusion LM. Block-autoregressive multi-canvas sampling. Use for: production-grade architecture reference, understanding how diffusion is adapted to text at scale.

- **DiffuMamba: *DiffuMamba: High-Throughput Diffusion LMs with Mamba Backbone*** — 2025
  [arXiv:2511.15927](https://arxiv.org/abs/2511.15927)
  Uses Mamba (SSM) backbone for diffusion. 8.2× speedup on long sequences. Use for: understanding SSM-based diffusion alternatives, cache-efficient decoding.

- **LLaDA: *Large Language Diffusion Models*** — ML-GSAI, 2025
  [GitHub](https://github.com/ML-GSAI/LLaDA) (3.9k+ stars)
  8B parameter masked diffusion model trained from scratch. **Most accessible large diffusion LM.** Use for: experimentation with a real diffusion LM at scale (quantization-friendly).

- **Transfusion: *Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model*** — Meta, 2024
  [arXiv:2408.11039](https://arxiv.org/abs/2408.11039)
  Combines next-token prediction + diffusion. Use for: understanding hybrid AR/diffusion approaches, scaling laws for multi-modal.

### Scaling Laws

- **SMDM: *Scaling up Masked Diffusion Models on Text*** — ML-GSAI, 2024
  [arXiv:2410.18514](https://arxiv.org/abs/2410.18514) | [Code](https://github.com/ML-GSAI/SMDM)
  **First scaling law for masked diffusion LMs.** Shows MDMs match ARMs in performance with 1.4× faster sampling. 1.1B MDM breaks the "reverse curse." Use for: understanding whether diffusion LMs scale like transformers.

### Surveys & Tutorials

- **DLLM Survey: *A Survey of Diffusion Language Models*** — 2025
  [arXiv:2506.13759](https://arxiv.org/abs/2506.13759) | [Curated Repo](https://github.com/LiQiiiii/DLLM-Survey) (387 stars)
  Comprehensive survey with categorized paper collection. Use for: bird's-eye view, finding relevant papers.

- **SEDD Simple Implementation (Colab)** — Yaghobzadeh
  [GitHub](https://github.com/emadyagh/Simple-Implementation-of-Score-Entropy-Discrete-Diffusion-SEDD-for-Text-Generation)
  Minimal SEDD with Colab notebook. Use for: hands-on learning, running on free GPU.

- **MDLM Video Tutorial** — Sahoo
  [Project Page](https://s-sahoo.com/mdlm) (includes blog post + video walkthrough)
  Best tutorial entry point for masked discrete diffusion.

- **Nemotron-Labs-Diffusion Tech Report** — NVIDIA, 2025
  [Tech Report PDF](https://d1qx31qr3h6wln.cloudfront.net/publications/Nemotron_Diffusion_Tech_Report.pdf) | [Code](https://github.com/NVlabs/Nemotron-Labs-Diffusion)
  Tri-mode (AR + diffusion + self-speculation) LMs at 3B, 8B, 14B sizes. Use for: understanding real-world deployment patterns, production hybrid architectures.

## Wisdom (Communities)

- **[r/MachineLearning](https://reddit.com/r/MachineLearning)** — Paper discussions; DiffusionGemma and LLaDA threads generate high engagement
- **[r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)** — Practical deployment discussions, quantization, running on consumer hardware
- **[Hugging Face Discord](https://huggingface.co/discord)** — `#diffusion` and `#text-generation` channels; model authors present
- **[LLaDA GitHub Discussions](https://github.com/ML-GSAI/LLaDA/discussions)** — Direct access to authors; active community
- **[DLLM-Survey Repo](https://github.com/LiQiiiii/DLLM-Survey)** — Curated paper list; PRs welcome; active tracking of the field

## Gaps

- No high-trust resource found comparing **training costs** (FLOPs, VRAM, time) of diffusion LMs vs autoregressive LMs at equivalent quality. We'll need to compile this ourselves from paper training details.
- No canonical "tiny diffusion LM from scratch" tutorial exists that fits in 8 GB VRAM — we'll create one.
- DiffuMamba code has not been publicly released; analysis limited to paper claims.
