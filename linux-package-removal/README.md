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
| 2 | [apt Removal, Done Right](./lessons/0002-apt-removal-done-right.html) | `remove` vs `purge` vs `autoremove`; reading a package's full footprint with `dpkg -L`. |
| 3 | [snap — Where the Bytes Hide](./lessons/0003-snap-cleanup.html) | The squashfs model, where disk space really goes, and pruning old revisions. |
| 4 | [The `/usr/local` Problem](./lessons/0004-usr-local-make-install.html) | Uninstalling a `make install` with no `make uninstall` — manifests, Stow, CheckInstall. |
| 5 | [Auditing Unowned Files](./lessons/0005-auditing-unowned-files.html) | Sweep the whole system for unmanaged files (`cruft`) and modified distro files (`debsums`). |

**Reference:** [Where Did This Come From? — Provenance & Removal cheat sheet](./reference/provenance-cheatsheet.html)

## Viewing the lessons

Lessons are standalone HTML — no build step, no server. The easiest way is the
`Makefile`, which generates a clickable index of every lesson and opens it:

```bash
make            # build index.html and open it in your browser (default)
make lessons    # open every lesson in its own tab, in order
make help       # list all targets
```

Or open a single file directly:

```bash
xdg-open lessons/0001-provenance-detective.html   # Linux
```

Each lesson links the shared stylesheet and quiz engine in [`assets/`](./assets/),
supports a light/dark toggle, and is designed to print cleanly for review.

## How to use it

1. Read the lesson top-to-bottom — it's short by design (working memory is small).
2. Do the interactive drills; the feedback is immediate.
3. Run the "on your own machine" task at the end — that's where the skill sticks.
4. Bring questions back to your teacher (the agent). That's the point of a stateful
   workspace: lessons build on what you've already shown you know.

---

<sub>Authored with the `teach` skill in Claude Code.</sub>
