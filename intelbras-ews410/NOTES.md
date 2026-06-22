# Working Notes — EWS 410 Local Control

## Learner profile
- Capable developer; comfortable in shell + Python (see the sibling
  `linux-package-removal/` course they completed). Skip basics; give precise
  protocol detail, mental models, edge cases.
- End goal is an **agent-callable tool**, so every lesson should ladder toward a
  clean CLI the harness can shell out to — not app-free clicking for its own sake.

## Teaching preferences
- On the previous course they preferred **all lessons up front** ("why would you
  wait?"). Flagged the tension here: this topic is **hardware-in-the-loop** —
  Lesson 2 needs a successful scan, Lesson 3 needs the real protocol version &
  local key, etc. So I built Lesson 1 fully and laid out the arc; offered to batch
  the rest. Revisit their preference once Lesson 1 runs against the real bulb.

## Course arc (planned)
1. ✅ The lay of the land — Tuya mental model, install tinytuya, scan → IP + device ID. [keystone]
2. ✅ The local key, offline — read key from the Intelbras app's on-phone cache; NO cloud API. Win: devices.json.
3. ⬜ First local command — BulbDevice on **v3.5**, on/off/colour/brightness/temp; DP map. Win: toggle, 100% offline.
4. ⬜ Wrap it as an agent tool — argparse CLI `lamp on|off|color|...`, JSON output, idempotency, error handling. Win: harness calls it.
5. ⬜ (Maybe) Robustness & multiple bulbs — IP drift / DHCP reservation, key rotation recovery, status polling, config file.

## Decisions locked (see learning-record 0002)
- Route: **100% local / no cloud API**. Read key from app's on-phone cache (MMKV/XML).
- Learner: Fairphone, not rooted, but **can access app data folders**; Intelbras app installed & controlling bulbs.
- Real device facts: **2 bulbs, both v3.5** — 192.168.1.16 (`eb402aa51227ed67cbnwj4`), 192.168.1.17 (`eba18068361d2cd57fbkwv`).
- Build Lesson 3 once the learner confirms extracted keys + a working devices.json.

## Device facts to confirm against hardware
- Protocol version (expect 3.3; could be 3.4/3.5 on newer firmware) — from real scan.
- DP map for power/mode/brightness/colour/temp — empirically once control is up.
- Whether bulb IP is pinned (DHCP reservation) — affects tool design in Lesson 4/5.

## Tooling / style
- Shared `assets/lesson.css` + `assets/quiz.js` copied from the Linux course for a
  consistent look + the same `initQuiz(FEEDBACK, {perfect, partial})` engine. Don't
  re-inline quiz logic.
- `Makefile`: `make` builds+opens index.html (generated, gitignored).
- Reference: `reference/tuya-local-cheatsheet.html` — keep authoritative; update the
  DP map / protocol version once known from the real device.

## Honest framing to preserve
- "No API" = no cloud **at control time**. The easy key-fetch touches cloud once.
  This is stated in MISSION.md and Lesson 1's callout — keep it honest, don't oversell.
