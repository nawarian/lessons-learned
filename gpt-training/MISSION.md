# Mission: Train a GPT from scratch, then fine-tune open-weight models

## Why
I want the operational understanding of how training really works — the full
pipeline from raw text to a model that generates tokens. Once I have that
foundation, I'll extend it to fine-tune open-weight models (like Qwen, DeepSeek,
Llama) for agentic coding tasks in Brazilian Portuguese.

## Success looks like
- I can write and explain every stage of a tiny GPT training pipeline: data
  loading → tokenization → model definition → training loop → inference.
- I have a working GPT trained on a small dataset, running locally on my L40S.
- I can take an open-weight model and fine-tune it on a pt-br coding dataset
  without cargo-culting a script I don't understand.
- I can read PyTorch training code for transformers and reason about what each
  component does.
- I can look at MoE architectures and understand how they differ from dense
  transformers (deferred to later, not now).

## Constraints
- Experienced software engineer; comfortable with Python and basic PyTorch.
- No deep learning theory background — cannot explain backpropagation or
  transformers at the architecture level.
- Familiar with LLM _user_ terminology (temperature, KV-cache, quantization,
  multimodal) but not the internals.
- Hardware: 8 GB VRAM desktop (experiments), L40S / 48 GB VRAM cloud (real
  training). L40S is always available on-demand.
- Learning style: hands-on, code-first. Prefer running real code over reading
  theory.

## Out of scope (for now)
- RLHF / preference tuning
- Quantization
- Multimodal models
- Production deployment (serving, batching, Triton, etc.)
- MoE architecture — explicitly deferred for later exploration
