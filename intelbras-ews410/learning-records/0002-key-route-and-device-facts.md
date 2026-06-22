# 0002 — Key route chosen + real device facts

- **Date:** 2026-06-21
- **Status:** Active
- **Supersedes nothing; extends 0001.**

## Decision: 100% local, no cloud API for the key
Learner explicitly rejected the easy cloud-wizard key fetch. Chose the
**rooted-Android cache-read** route: read the local key out of the Intelbras/Izy
app's own on-phone storage. No Tuya IoT developer project, no API credentials, no
recurring cloud dependency.

## Key conceptual point established
A Tuya local key is a **random value assigned by the cloud at pairing** — it
cannot be derived/computed, only *read* from somewhere it's already stored. Every
"get the key" method is really "read it from a device that already has it" (your
phone, the developer API, or sniffed traffic). True never-touched-cloud requires
reflashing firmware (out of scope for now).

## Learner's setup (matters for the lesson)
- Phone: **Fairphone**, running the **Intelbras (Izy Smart) app** that already
  controls the bulbs — so the keys are cached on it.
- **Not rooted**, but learner says they **can access the app's data/cache folders**.
  So the lesson is method-agnostic on *retrieval* (get the one file off the phone)
  and precise on *parsing* (extract cleartext keys from it).

## Real device facts (from learner's `tinytuya scan`)
- **Two bulbs**, same module (Product ID `key8u54q9dtru5jw`):
  - `192.168.1.16` — Device ID `eb402aa51227ed67cbnwj4`
  - `192.168.1.17` — Device ID `eba18068361d2cd57fbkwv`
- **Both protocol v3.5** (newest Tuya wire format; has a session handshake).
  tinytuya supports 3.5 — note for Lesson 3 control calls.
- Local keys still unknown — Lesson 2's target.

## Implications
- Tool must address **multiple bulbs** by ID (matches mission).
- IPs `.16/.17` came from DHCP — confirm a reservation later (Lesson 5) so the
  tool doesn't break when they drift.
