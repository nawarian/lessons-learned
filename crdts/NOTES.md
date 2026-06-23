# Teaching Notes — CRDTs

## Preferences
- **Code-first.** Lead every lesson with runnable JS the user can paste into a
  console / Node and *watch two replicas converge*. Theory (lattices, commutativity,
  monotonicity) comes in only to explain why the code is correct — not up front.
- Keep lessons short; one tangible win each; always tie back to the **whiteboard**.
- Strong dev background — skip programming basics, pitch at precise mental models.

## Mission anchor
User's harness is building a **collaborative whiteboard** (shapes on a shared
canvas, p2p / offline-first). Map every CRDT concept onto a whiteboard concern:
- shape property (color, x/y) → register (LWW-Register)
- the set of shapes present → add/remove set (OR-Set) — delete vs concurrent edit
- a shape's full record → map of registers
- z-order / text in a note → sequence CRDT (RGA / YATA)

## Planned arc (subject to ZPD revision)
1. The convergence promise + LWW-Register on a shape property  ← built first
2. The merge law: commutative/associative/idempotent = a semilattice; state- vs op-based
3. Sets of shapes: G-Set → 2P-Set → OR-Set (the delete-vs-edit problem, tombstones)
4. A shape as a map of registers; nested CRDTs
5. Sequences: ordering & text — RGA / YATA, "the hard parts"
6. Real libraries (Yjs / Automerge), GC, the network

## Open questions to revisit
- Does their whiteboard already use a library (Yjs/Automerge) or a hand-rolled model?
  This changes whether Lesson 6 is "read the source" or "you built this, let's audit it."
