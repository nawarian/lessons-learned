# Lessons Learned

A personal, stateful learning workspace. Each topic is taught through short,
self-contained **lessons** grounded in a single **mission** — the real-world
reason for learning it — and backed by **reference** cheat sheets you return to
later.

> **Current mission:** confidently declutter a Linux machine — look at anything
> installed and know where it came from (apt, snap, `make install`, or a manual
> symlink), then remove it cleanly without leaving orphans behind.
> See [`MISSION.md`](./MISSION.md).

## How this workspace is organized

| Path | What lives here |
| --- | --- |
| [`MISSION.md`](./MISSION.md) | The *why* — the concrete goal every lesson traces back to. |
| [`lessons/`](./lessons/) | The main unit of teaching: one tightly-scoped, interactive HTML lesson each. |
| [`reference/`](./reference/) | Compressed cheat sheets — the bits worth keeping open while you work. |
| [`learning-records/`](./learning-records/) | What's been learned / established, so future sessions pitch at the right level. |
| [`RESOURCES.md`](./RESOURCES.md) | Curated, high-trust sources (and communities) the lessons draw from. |
| [`assets/`](./assets/) | Shared components — e.g. `lesson.css`, the common stylesheet. |
| `NOTES.md` | Scratchpad for preferences and the provisional course arc. |

## Lessons

| # | Lesson | One-line | 
| --- | --- | --- |
| 1 | [The Provenance Detective](./lessons/0001-provenance-detective.html) | Classify any command into apt / snap / make-install / manual-symlink — the keystone skill behind every clean uninstall. |

**Reference:** [Where Did This Come From? — Provenance & Removal cheat sheet](./reference/provenance-cheatsheet.html)

## Viewing a lesson

Lessons are standalone HTML — no build step, no server. Open one in a browser:

```bash
xdg-open lessons/0001-provenance-detective.html   # Linux
```

Each lesson links the shared stylesheet in [`assets/`](./assets/), supports a
light/dark toggle, and is designed to print cleanly for review.

## How to use it

1. Read the lesson top-to-bottom — it's short by design (working memory is small).
2. Do the interactive drills; the feedback is immediate.
3. Run the "on your own machine" task at the end — that's where the skill sticks.
4. Bring questions back to your teacher (the agent). That's the point of a stateful
   workspace: lessons build on what you've already shown you know.

---

<sub>Authored with the `teach` skill in Claude Code.</sub>
