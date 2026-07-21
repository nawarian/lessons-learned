# Diffusion Language Models — Glossary

Core terminology used throughout this workspace. Adhere to these definitions in lessons and reference materials.

## Concepts

**Autoregressive generation**:
A decoding strategy where each token is generated conditioned on all previous tokens, one at a time. The canonical approach for GPT-family models.
_Avoid_: Sequential generation, left-to-right generation

**Forward diffusion process**:
A noising process that gradually corrupts data (text, images) into pure noise over a sequence of timesteps, according to a fixed variance schedule.
_Avoid_: Noising schedule, corruption process

**Reverse diffusion process (denoising)**:
A learned process that predicts and removes noise step by step, starting from pure noise and recovering structured data.
_Avoid_: The generative process

**Discrete token space**:
The set of all possible tokens in a vocabulary — a finite, categorical set with no inherent ordering or metric structure.
_Avoid_: Vocabulary space, token set (when talking about the space itself)

**Continuous embedding space (latent space)**:
A vector space (typically ℝᵈ) where tokens are embedded before processing. The diffusion process operates in this space, not on discrete tokens directly.
_Avoid_: Hidden space, embedding vector (when talking about the space)

**Masked diffusion**:
A form of discrete diffusion where the forward process gradually masks tokens (replacing them with a special [MASK] token), and the reverse process predicts the original tokens.
_Avoid_: Masked language modeling (MLM) — MLM is bidirectional but not a diffusion process

**Scaling law**:
An empirical relationship showing that model performance improves predictably with increased model size, dataset size, and compute, typically following a power-law trend.
_Avoid_: Scaling curve, scaling behavior

## Architectures

**Transformer**: 
A neural architecture based on self-attention mechanisms, processing all tokens in parallel during training but generating autoregressively during inference.

**State Space Model (SSM)**:
A sequence model that maps an input sequence to an output sequence through a latent state, using structured matrices for efficient computation. The basis of the Mamba architecture.
_Avoid_: S4 (S4 is a specific SSM variant, not the general class)

**Diffusion Transformer (DiT)**:
A transformer whose core computation is a denoising step applied to a noisy latent representation, rather than predicting the next token.
_Avoid_: DiT (when referring to text models — DiT is primarily for images)

**Mamba**:
A selective state space model architecture that achieves linear-time sequence modeling with a data-dependent state. The backbone of DiffuMamba.

**DiffusionGemma**:
A family of diffusion language models from Google DeepMind based on the Gemma transformer backbone, trained to denoise rather than predict next tokens.

**DiffuMamba**:
A diffusion language model that uses a Mamba (SSM) backbone for the denoising process, aiming for linear-complexity diffusion.

## Cost Metrics

**FLOP** (Floating Point Operation):
A basic unit of computational work. Model training costs are typically measured in petaFLOP-days or exaFLOP-seconds.

**VRAM** (Video RAM):
GPU memory that holds model parameters, activations, optimizer states, and gradients during training. The primary constraint for single-GPU training.

**Perplexity** (PPL):
A standard metric for language model quality. Lower is better. For diffusion LMs, often reported as "bits per byte" or "negative log-likelihood."
