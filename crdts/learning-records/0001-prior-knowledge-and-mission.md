# Prior knowledge & mission established

The user is a strong developer (shell/dev background, JS for this project). Their
agentic harness is actively building a **CRDT-based collaborative whiteboard**, and
the goal is a **mental model strong enough to reason about that implementation** —
not to ship a library or a transport layer. They explicitly want **code-first**
teaching: runnable code first, theory only to justify it.

Implications for future sessions:
- Anchor every CRDT family to a concrete whiteboard concern (see [[NOTES.md]]).
- Don't open with lattice algebra; introduce the merge laws *after* the user has
  watched code converge.
- Find out whether the whiteboard uses an existing library or a hand-rolled model —
  it decides the shape of the later lessons. (Open question in NOTES.)
