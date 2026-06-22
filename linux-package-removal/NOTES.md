# Working Notes

## Learner profile
- Self-rates **fairly advanced** with shell & filesystem. Skip CLI basics
  (cd/ls/cat). Give precise mental models, edge cases, the *why*.
- Mission is **decluttering**: every lesson should end with something they can
  actually run on their own machine to find or remove cruft.

## Teaching preferences
- Prefers the **whole set of lessons up front** over one-at-a-time drip. Asked
  "why would you wait?" — wants to self-pace through all material. Build ahead;
  revise lessons after they run them on real machine output rather than gating
  release on evidence. (Trade-off accepted: less adaptivity.)

## Course arc — ALL BUILT
1. ✅ Provenance detective — classify any command into one of 4 sources. [keystone]
2. ✅ apt removal done right — remove vs purge vs autoremove; `dpkg -L`.
3. ✅ snap — list --all, revisions, squashfs/var, clean removal + --purge.
4. ✅ The `/usr/local` problem — make uninstall / manifest / stow / checkinstall.
5. ✅ Auditing unowned files — cruft + debsums/dpkg --verify, false positives.

## Possible future lessons
- Interleaving review: mixed-source classify-and-remove drills (spacing/recall).
- Adjacent install methods currently out of scope but likely to come up:
  pip/npm -g, AppImage, Flatpak, update-alternatives. Lesson 1 ask-box invites these.

## Tooling
- `assets/quiz.js`: shared quiz engine — `initQuiz(FEEDBACK, {perfect, partial})`.
  All 5 lessons use it. Don't re-inline quiz logic in new lessons.
- `Makefile`: `make` builds+opens index.html (generated, gitignored); `make
  lessons` opens all tabs; `make index` regenerates from lessons/ + reference/.
6. (Maybe) interleaving review — mixed-source classify + remove drills.

## Style
- Shared CSS: assets/lesson.css (Tufte-ish, serif, light/dark).
- Reference: reference/provenance-cheatsheet.html — keep authoritative; update
  whenever a lesson refines the decision tree.
