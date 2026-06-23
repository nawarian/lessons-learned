# CRDT Resources

Trust labels: **[Primary]** original source/author · **[Expert]** recognized
practitioner/maintainer · **[Vendor]** official product docs.

## Knowledge

### Start here (intuition)
- [An Interactive Intro to CRDTs — Jake Lazaroff](https://jakelazaroff.com/words/an-interactive-intro-to-crdts/) **[Expert]**
  Live, embedded playgrounds: toggle the network, watch replicas merge, build from
  an LWW register up to a collaborative pixel editor. Use for: the very first,
  zero-background intuition — closest thing to our whiteboard.
- [crdt.tech — the CRDT research hub](https://crdt.tech/) ([glossary](https://crdt.tech/glossary) · [papers](https://crdt.tech/papers.html)) **[Primary/Expert]**
  Curated by Kleppmann, Bieniusa & Shapiro. Use for: the authoritative one-line
  definitions (state- vs op-based, etc.) and as a jump-off to every paper.

### Foundational theory (Shapiro et al.)
- [Conflict-free Replicated Data Types — SSS 2011 (PDF)](https://asc.di.fct.unl.pt/~nmp/pubs/sss-2011.pdf) **[Primary]**
  The citable, condensed paper. Formalizes state-based vs op-based and the
  convergence conditions. Use for: a focused reading assignment on *why* it works.
- [A comprehensive study of CvRDTs and CmRDTs — INRIA RR-7506 (PDF)](https://inria.hal.science/inria-00555588/PDF/techreport.pdf) **[Primary]**
  The definitive 50-page catalog (registers, counters, sets, graphs, sequences)
  with proofs. (HAL is bot-walled; working mirror:
  [Berkeley CS286 PDF](https://dsf.berkeley.edu/cs286/papers/crdt-tr2011.pdf).)
  Use for: looking up the canonical design of any specific CRDT.

### Martin Kleppmann (recognized expert)
- [CRDTs: The Hard Parts — talk](https://martin.kleppmann.com/2020/07/06/crdt-hard-parts-hydra.html) ([video](https://www.youtube.com/watch?v=PMVBuMK_pJY) · [slides](https://speakerdeck.com/ept/crdts-the-hard-parts)) **[Primary/Expert]**
  Anomalies, interleaving bugs, and performance traps in published algorithms. Use
  for: inoculation against naive implementations *after* the fundamentals.
- [Cambridge Concurrent & Distributed Systems — lecture notes (PDF)](https://www.cl.cam.ac.uk/teaching/2425/ConcDisSys/dist-sys-notes.pdf) **[Primary/Expert]**
  Places CRDTs in the broader consistency/replication picture. Use for: theoretical
  grounding (causality, vector clocks).

### Build-the-structures (implementation)
- [Bartosz Sypytkowski — CRDT series](https://www.bartoszsypytkowski.com/tag/crdt/) (start: [state-based CRDTs](https://www.bartoszsypytkowski.com/the-state-of-a-state-based-crdts/)) **[Expert]**
  11+ parts implementing GCounter/PNCounter, OR-Set, vector clocks, delta-state,
  op-based arrays, JSON (F#, but the algorithms port directly). Author is a Yjs/Yrs
  core contributor. Use for: when we actually build each data structure.

### Real-world implementations
- [Yjs](https://yjs.dev/) ([docs](https://docs.yjs.dev/) · [internals](https://docs.yjs.dev/api/internals) · [GitHub](https://github.com/yjs/yjs)) **[Primary]**
  The most widely deployed collaborative-editing CRDT lib. Use for: reading real
  source; the likely engine under a JS whiteboard.
- [YATA paper — Near Real-Time P2P Shared Editing (2016)](https://www.researchgate.net/publication/310212186_Near_Real-Time_Peer-to-Peer_Shared_Editing_on_Extensible_Data_Types) **[Primary]**
  The sequence-CRDT algorithm behind Yjs. Use for: how collaborative *ordering*
  (z-order / text) actually resolves.
- [Automerge](https://automerge.org/) ([docs](https://automerge.org/docs/)) **[Primary]**
  JSON-CRDT local-first sync engine (Kleppmann / Ink & Switch). Use for: the
  document-shaped alternative to Yjs.
- [Redis Active-Active CRDTs](https://redis.io/docs/latest/operate/rs/databases/active-active/) ([intro](https://redis.io/blog/diving-into-crdts/)) **[Vendor]** ·
  [Riak KV Data Types](https://docs.riak.com/riak/kv/latest/learn/concepts/crdts/index.html) **[Vendor]** (historically important; product now legacy)
  Use for: "CRDTs at industrial scale" context.

## Wisdom (Communities)
- [Local-First Software — the founding essay (Ink & Switch, 2019)](https://www.inkandswitch.com/essay/local-first/) **[Primary]**
  Coins "local-first" and frames *why* CRDTs matter. Essential context reading.
- [localfirst.fm — podcast](https://www.localfirst.fm/) · [Local-First Conf](https://www.localfirstconf.com/) **[Expert]**
  Practitioners on real-world tradeoffs. Use for: keeping current, hearing war stories.
- [Yjs community forum](https://discuss.yjs.dev/) **[Primary]**
  Implementation Q&A direct from maintainers. Use for: concrete whiteboard/Yjs bugs.
- [LoFi.so — Local-First Discord](https://discord.com/invite/ZRrwZxn4rW)
  Main active practitioner chat (~3.8k). ⚠️ invite codes rotate — re-verify the link.
- [awesome-local-first](https://github.com/alexanderop/awesome-local-first) **[Community]**
  Curated directory of tools/resources.

## Gaps
- No whiteboard-specific CRDT writeup found yet (most material is text-editor
  focused). We bridge that gap ourselves in the lessons.
- Haven't yet confirmed whether the user's whiteboard uses Yjs/Automerge or a
  hand-rolled model — drives whether late lessons read library source or audit theirs.
