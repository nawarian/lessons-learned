# Lessons Learned

A personal, stateful learning workspace taught by my agentic harness. Each
**topic** lives in its own folder and is a self-contained course: short,
interactive HTML **lessons** grounded in a single **mission** (the real-world
reason for learning it), backed by **reference** cheat sheets you return to later.

## Topics

| Folder | Mission | Status |
| --- | --- | --- |
| [`linux-package-removal/`](./linux-package-removal/) | Confidently declutter a Linux machine — know where any installed thing came from, then remove it cleanly. | 5 lessons (complete) |
| [`intelbras-ews410/`](./intelbras-ews410/) | Control the Intelbras EWS 410 lamp **locally** so an agentic harness can change the lights on prompt. | Lesson 1 (in progress) |
| [`crdts/`](./crdts/) | Grok CRDTs well enough to reason about a p2p, offline-first collaborative whiteboard the harness is building. | Lesson 1 (in progress) |
| [`gpt-training/`](./gpt-training/) | Train a GPT from scratch, then fine-tune open-weight models for agentic coding in pt-br. | Lesson 1 (just started) |
| [`diffusion-lm/`](./diffusion-lm/) | Understand, train, and fine-tune diffusion-based language models for text generation on Brazilian hardware (L40S). Build a 300M distilled MDLM for Portuguese + English + agentic coding. | 8 lessons (complete) 🏁 |

## How each topic folder is organized

| Path | What lives here |
| --- | --- |
| `MISSION.md` | The *why* — the concrete goal every lesson traces back to. |
| `lessons/` | The main unit of teaching: one tightly-scoped, interactive HTML lesson each. |
| `reference/` | Compressed cheat sheets — the bits worth keeping open while you work. |
| `learning-records/` | What's been learned / established, so future sessions pitch at the right level. |
| `assets/` | Shared `lesson.css` + `quiz.js` — consistent look and one quiz engine. |
| `RESOURCES.md` | High-trust sources (knowledge) and communities (wisdom). |
| `NOTES.md` | Teaching preferences and working notes. |
| `Makefile` | `make` builds + opens an index of that topic's lessons in your browser. |

## Browsing a topic

```sh
cd <topic-folder> && make        # builds index.html and opens it
make lessons                     # open every lesson in its own tab
```
