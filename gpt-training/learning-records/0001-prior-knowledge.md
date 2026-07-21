# 0001: Prior knowledge established — software engineering foundations

The user is an experienced software engineer comfortable with Python and basic
PyTorch. They have first-hand familiarity with high-level LLM concepts
(temperature, KV-cache, quantization, multimodal) from using agentic harnesses
and LLMs, but cannot explain the internal architecture of transformers or the
mechanics of backpropagation.

**Implications:** Lessons should not spend time on Python/PyTorch syntax,
environment setup, or version management. They should also not waste cycles
explaining LLM concepts the user already grasps at the product level. Every
lesson should focus on the _internal mechanics_ — the things that happen between
the API call and the generated token, which the user has never seen from the
outside. The first lesson (pipeline overview) provides a map; subsequent lessons
fill in the blank cells of that map one at a time.
