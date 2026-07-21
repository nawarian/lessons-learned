# GPT Training Resources

## Knowledge

- [Video: "Let's build GPT from scratch" — Andrej Karpathy](https://www.youtube.com/watch?v=kCc8FvEb1nY)
  The canonical walkthrough. Builds a GPT in pure PyTorch from first principles.
  Use for: understanding every component of the training pipeline we run.

- [Repo: nanoGPT — Andrej Karpathy](https://github.com/karpathy/nanoGPT)
  The minimal, production-quality GPT implementation. Our script is a simplified
  version of this. Use for: reference implementation, scaling up.

- [Paper: "Attention Is All You Need" — Vaswani et al. (2017)](https://arxiv.org/abs/1706.03762)
  The original transformer paper. Use for: the authoritative description of the
  architecture (read after you've run the code, not before).

- [Blog: "The Illustrated Transformer" — Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
  The most accessible visual explanation of transformer internals.
  Use for: building intuition before diving into the math.

- [Blog: "The Illustrated GPT-2" — Jay Alammar](https://jalammar.github.io/illustrated-gpt2/)
  Visual walkthrough of how GPT-2 generates text step by step.
  Use for: understanding inference-time behaviour.

- [Tutorial: "Understanding and Training a GPT" — Cameron Smith](https://cameronrwsmith.me/blog/gpt-from-scratch)
  Clear tutorial covering data preparation, training, and generation.
  Use for: an alternative explanation style when something clicks differently.

- [Documentation: PyTorch `nn.Transformer`](https://pytorch.org/docs/stable/nn.transformer.html)
  PyTorch's built-in transformer module docs. Use for: looking up exact API
  signatures when implementing from scratch.

- [Documentation: Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
  The standard library for working with open-weight models. Use for: fine-tuning
  phase (later in the curriculum).

- [Tutorial: "Fine-tuning a Language Model" — Hugging Face](https://huggingface.co/learn/nlp-course/chapter7/6)
  Step-by-step fine-tuning guide using the Transformers library.
  Use for: bridging from scratch training to fine-tuning (after Lesson 7).

- [Web: "The GPT-3 Architecture" — Gwern](https://gwern.net/gpt-3)
  Deep analysis of GPT-3/4 architecture decisions. Use for: understanding what
  changes when scaling from our tiny model to production models.

## Wisdom (Communities)

- [r/MachineLearning](https://reddit.com/r/MachineLearning)
  General ML discussion. Use for: staying current with techniques, asking
  architecture-level questions.

- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  Community focused on running and fine-tuning open-weight models.
  Use for: practical advice on fine-tuning, hardware requirements, and tooling.

- [Hugging Face Discord](https://discord.gg/huggingface)
  Active community around open models. Use for: real-time help with
  Transformers library, fine-tuning setup.

- [PyTorch Forums](https://discuss.pytorch.org/)
  Official PyTorch community. Use for: debugging training code, understanding
  specific PyTorch behaviours.

## Gaps

- No single trusted resource found yet specifically covering _operational_
  aspects of training (cost estimation, dataset curation, experiment tracking).
  This may be filled by community knowledge or blog posts discovered during
  the course.

## Community preferences

- The user is comfortable joining online communities for help.
