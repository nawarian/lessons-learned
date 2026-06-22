# Mission: Local, Agent-Driven Control of the Intelbras EWS 410 Lamp

## Why
I want to give my **agentic harness** a tool it can call to change the lights in
my environment — e.g. prompt "dim the room to warm white" and have the agent
actually do it. The lamp (Intelbras EWS 410) is controlled today only through
Intelbras's *Izy Smart* app, which talks to the cloud. I want to drive it
**locally**, without depending on the vendor's cloud API at control time, so the
agent's commands are fast, private, and work even if the internet is down.

## What the device actually is
The EWS 410 is a **Tuya-platform** Wi-Fi bulb (Izy/Mibo Smart is Intelbras's
rebrand of Tuya). Wi-Fi 2.4 GHz only for control; the Bluetooth 4.2 is used for
provisioning, not day-to-day control. This matters: it means the mature Tuya
**local LAN** toolchain (`tinytuya`, LocalTuya) applies directly.

## Success looks like
- My agent can run a single shell command (a small CLI I own) to turn the lamp
  on/off, set brightness, color, and color temperature — and it works on the LAN
  with **no cloud round-trip** at control time.
- I understand the three secrets local control needs — **device ID, LAN IP,
  local key** — where each comes from, and which can change.
- I can recover control if the bulb's IP changes, the app is reinstalled, or the
  local key rotates.
- I can explain the Tuya local protocol well enough to debug it (encryption,
  protocol version 3.3/3.4/3.5, data points / "DPs").

## The honest constraint
"Without their API" means **no cloud at control time**. Getting the local key
the *easy* way still touches Tuya's cloud **once** (a free developer account read
of the key). Fully-offline key extraction (packet capture / app extraction) is
possible and will be covered as the harder alternative. The end state — control —
is always 100% local.

## Constraints
- Strong shell/dev background. Skip basics; want the precise mental model,
  protocol detail, and edge cases. Python is fine for the tooling.
- One known bulb to start; design the tool so it scales to several.
- Linux (Ubuntu) workstation as the controller.

## Out of scope (for now)
- Custom firmware flashing (Tuya-Convert / ESPHome / LibreTiny) — a deeper de-cloud
  path, noted but not the first goal.
- Zigbee/Matter (this device is neither).
- Building a full Home Assistant deployment (we want a lean, agent-callable tool).
