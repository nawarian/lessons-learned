# 0002: Forward/backward taught at Lesson 2 (pulled forward from planned Lesson 6)

After running the Lesson 1 pipeline, the user asked — unprompted — about the
`GPT(nn.Module)` class overriding `forward()`, and `loss.backward()`, correctly
sensing they were PyTorch mechanics related to forward/backward propagation.

I judged this squarely in the zone of proximal development and the conceptual
core of the mission ("how does training really work?"), so I taught it now as
**Lesson 2 · Forward & Backward** rather than deferring to the originally-planned
Lesson 6. The remaining planned sequence (tokenizer, embeddings, attention,
transformer block) is unchanged; the training-loop lesson is now effectively done.

**What the lesson established:**
- The two-pass cycle: forward pass (forward propagation) = `forward()` producing
  logits; backward pass (backpropagation) = `loss.backward()` computing gradients.
- `nn.Module` gives parameter registration, device/mode plumbing, and `__call__`.
- Why `model(x)` not `model.forward(x)` (the `__call__` wrapper).
- Autograd records a computation graph during the forward pass; `backward()` walks
  it in reverse via the chain rule, filling `p.grad` (directions only, no update).
- The three-line dance: `zero_grad()` → `backward()` → `step()`, and why order
  and `zero_grad()` matter.
- Created reference: `training-step-cheatsheet.html`.

**Open threads the user can pull next (flagged in the lesson):**
- Chain rule on a toy two-weight example.
- What AdamW adds over plain SGD (momentum, per-weight scaling).
- `requires_grad` and `torch.no_grad()` — the latter already used in `generate()`.

**Implications for sequencing:** the optimizer (`AdamW`, learning rate, momentum)
was deliberately left as a black box ("sets the step size"). If the user bites on
the AdamW thread, that's the natural next lesson; otherwise resume the architecture
track (tokenizer → embeddings → attention).
