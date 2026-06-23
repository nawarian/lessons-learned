# Mission: Grok CRDTs to Reason About a Collaborative Whiteboard

## Why
My agentic harness is currently building a **CRDT-based collaborative whiteboard**
app — multiple people drawing shapes on a shared canvas, syncing peer-to-peer and
offline-first. I need a strong enough **mental model** of how CRDTs work that I can
*reason about that implementation*: judge whether the data model is right, spot
where it will lose updates or diverge, and debug sync bugs when two boards don't
end up identical.

## Success looks like
- I can explain **why** two whiteboards that received the same edits in different
  orders (or with duplicates, or after an offline gap) end up byte-for-byte
  identical — and what property of the merge function guarantees that.
- Given a whiteboard concern — "move a shape", "delete a shape someone else is
  editing", "two people recolor the same shape", "z-order of overlapping shapes",
  "text inside a sticky note" — I can name which **kind of CRDT** fits and why.
- I can read the source of a real CRDT library (Yjs / Automerge) and follow what
  it's doing instead of treating it as magic.
- I can predict the failure modes: lost updates, resurrected deletes, unbounded
  tombstone growth — and how each CRDT family trades them off.

## Constraints
- Strong shell/dev background; JS is the working language for the whiteboard.
  **Code-first** — lead with runnable code I can paste and watch merge; bring in
  the theory (commutativity, semilattices, monotonicity) only to explain *why* the
  code works.
- Lessons stay short and tied back to the whiteboard.

## Out of scope (for now)
- Building a production network/transport layer (WebRTC, sync servers) — the focus
  is the data-structure reasoning, not the wire.
- Byzantine fault tolerance / security of the sync protocol.
- Writing a brand-new sequence CRDT from scratch — we'll understand existing ones
  (RGA / YATA), not invent one.
