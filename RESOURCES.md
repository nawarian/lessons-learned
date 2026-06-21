# Linux Filesystem & Clean Package Removal — Resources

## Knowledge

- [Filesystem Hierarchy Standard 3.0 (PDF) — Linux Foundation](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf)
  The primary, authoritative spec for what every top-level directory is *for*.
  Use for: the canonical meaning of `/usr`, `/usr/local`, `/opt`, `/var`, `/etc`.
- [FHS — Wikipedia](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
  Readable summary table of the hierarchy. Use for: a quick refresher on any path.
- [dpkg-query(1) man page — man7.org](https://man7.org/linux/man-pages/man1/dpkg-query.1.html)
  Authoritative reference for `dpkg -S`, `-L`, `-l`, `-V`. Use for: proving which
  apt package owns a file, and listing everything a package installed.
- [apt remove vs purge vs autoremove — It's FOSS](https://itsfoss.com/apt-remove-purge/)
  Clear, correct breakdown of the three removal verbs. Use for: deciding remove
  vs purge, and cleaning orphaned dependencies.
- [GNU Stow — official manual](https://www.gnu.org/software/stow/manual/stow.html)
  The symlink-farm manager for sane manual installs into `/usr/local`. Use for:
  installing from source so it's trivially uninstallable later.
- [Using GNU Stow to manage manually compiled software — Hetzner Community](https://community.hetzner.com/tutorials/using-gnu-stow-to-manage-manually-compiled-software/)
  Practical end-to-end `./configure --prefix` → stow → unstow workflow.
- [Clean up snap packages — It's FOSS](https://itsfoss.com/clean-snap-packages/)
  `snap list --all`, removing old revisions, where snaps live. Use for: snap
  disk usage and revision cleanup.
- [CheckInstall — Debian Wiki](https://wiki.debian.org/CheckInstall)
  Wraps `make install` to produce a real .deb so source builds become
  apt-removable. Use for: making future source installs trackable.
- [CheckingDebsums — Debian Wiki](https://wiki.debian.org/CheckingDebsums)
  `debsums` verifies installed files against dpkg's recorded md5sums. Use for:
  finding distro files that were modified or are missing.
- [cruft — Debian Wiki / package](https://packages.debian.org/stable/cruft)
  Lists files on disk that no package owns. Use for: hunting truly unmanaged
  cruft (with care — many false positives).

## Wisdom (Communities)

- [r/linuxquestions](https://reddit.com/r/linuxquestions)
  Broad, beginner-friendly but technically solid. Use for: "is it safe to remove
  X?" sanity checks.
- [Unix & Linux Stack Exchange](https://unix.stackexchange.com/)
  High-signal, heavily-moderated Q&A. Use for: precise questions about provenance,
  dpkg internals, FHS edge cases. Search before asking — usually already answered.
- [Ask Ubuntu](https://askubuntu.com/)
  Ubuntu-specific. Use for: apt/snap behaviour particular to Ubuntu releases.

## Gaps
- (none open — `debsums` / `cruft` sources added for the auditing lesson.)
