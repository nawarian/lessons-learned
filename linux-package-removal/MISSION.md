# Mission: Linux Filesystem & Clean Package Removal

## Why
My machine has accumulated cruft — duplicate tools, leftover files, things I
installed once and forgot. I want to confidently look at anything on my system,
know where it came from (apt, snap, a manual symlink, or `make install`), and
remove it cleanly without leaving orphans or breaking other software.

## Success looks like
- Given any command on my `PATH`, I can determine in under a minute which of the
  four sources installed it — and prove it, not guess.
- I can remove an apt package *and* its config and orphaned dependencies, not
  just the binary.
- I can clean up a `make install` that has no `make uninstall`.
- I can audit `/usr/local` and `/opt` and explain every file there.
- I never again "delete the binary" and leave libs, configs, and data behind.

## Constraints
- Fairly advanced with the shell already — wants the precise mental model and
  edge cases, not command-line basics.
- Primarily an Ubuntu/Debian-family machine (apt + snap present).

## Out of scope (for now)
- Building .deb packages from scratch.
- Containers / Docker image layers.
- Non-Debian package managers (pacman, dnf, nix) beyond passing mention.
