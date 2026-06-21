# Working Notes

## Learner profile
- Self-rates **fairly advanced** with shell & filesystem. Skip CLI basics
  (cd/ls/cat). Give precise mental models, edge cases, the *why*.
- Mission is **decluttering**: every lesson should end with something they can
  actually run on their own machine to find or remove cruft.

## Teaching preferences
- (none stated yet — update as they emerge)

## Course arc (provisional)
1. ✅ Provenance detective — classify any command into one of 4 sources. [keystone]
2. apt removal done right — remove vs purge vs autoremove; `dpkg -L` to inspect.
3. snap — list/all, revisions, where bytes live, clean removal.
4. The `/usr/local` problem — make install with no uninstall; manifests; stow.
5. Auditing unowned files — find cruft nothing manages (needs a good source first).
6. (Maybe) interleaving review — mixed-source classify + remove drills.

## Style
- Shared CSS: assets/lesson.css (Tufte-ish, serif, light/dark).
- Reference: reference/provenance-cheatsheet.html — keep authoritative; update
  whenever a lesson refines the decision tree.
