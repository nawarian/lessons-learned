# 0001 — Prior knowledge & mission established

- **Date:** 2026-06-21
- **Status:** Active

## Context
First session on this topic. Learner already has a separate, completed course in
this repo (Linux package removal), so they are a capable developer comfortable in
the shell and with Python tooling.

## What the learner wants
Control the Intelbras EWS 410 Wi-Fi lamp **locally**, so their **agentic harness**
can change the room's lights on prompt. The end deliverable is an agent-callable
tool (a small CLI), not just app-free clicking. Decided via /teach intake question.

## Key facts established this session
- The EWS 410 is a **Tuya-platform** device (Izy/Mibo Smart = rebadged Tuya).
  Confirmed via Intelbras specs + Tecnoblog review + HA Brasil forum.
- Control is **Wi-Fi 2.4 GHz only**; BLE 4.2 is for provisioning, not control.
- The mature local path is **`tinytuya`** (direct LAN), with `LocalTuya` as a
  cross-check. Control needs three secrets: **device ID, LAN IP, local key**.
- "Without their API" = no cloud **at control time**. The easy key-fetch still
  touches Tuya cloud **once**; fully-offline extraction exists as a harder path.
  Learner has accepted this framing (it's in MISSION.md).

## Workspace decision
Repo reorganized so **each topic gets its own folder**. Linux course moved to
`linux-package-removal/`; this topic lives in `intelbras-ews410/`. Shared assets
(`lesson.css`, `quiz.js`) copied in for a consistent look.

## Zone of proximal development
Skip networking/Python basics. Start at the **mental model + reconnaissance**
(what Tuya local control is; find the bulb on the LAN). Defer the cloud key-fetch,
the actual control calls, and tool-wrapping to subsequent lessons — each is gated
on real output from the learner's device.

## Open questions to resolve against the hardware
- Protocol version (3.3 / 3.4 / 3.5)?
- The bulb's DP map (power / mode / brightness / colour / temp)?
- Does the bulb get a DHCP reservation, or will its IP drift (affects the tool)?
