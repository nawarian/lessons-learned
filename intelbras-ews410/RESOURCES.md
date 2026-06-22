# Intelbras EWS 410 — Local Control — Resources

## Knowledge — the device

- [EWS 410 product page — Intelbras](https://www.intelbras.com/pt-br/lampada-led-smart-wi-fi-ews-410)
  Official specs. Use for: confirming Wi-Fi 2.4 GHz only, E27, RGB+CCT, BLE 4.2.
- [EWS 410 datasheet (PDF)](https://backend.intelbras.com/sites/default/files/2023-07/EWS%20410%20-%20Datasheet%20v2_0.pdf)
  Authoritative electrical/RF spec sheet.
- [Tecnoblog review — EWS 410](https://tecnoblog.net/testamos/smart-lampada-intelbras-ews-410-review/)
  Independent confirmation it's a Tuya/Izy device, 2.4 GHz only, no Zigbee.

## Knowledge — Tuya local protocol & tooling (the core)

- [tinytuya — GitHub (jasonacox)](https://github.com/jasonacox/tinytuya)
  **Primary tool.** Python lib + CLI for direct-LAN Tuya control. Use for:
  `scan`, the cloud `wizard` to fetch local keys, and `BulbDevice` control.
- [tinytuya — PyPI](https://pypi.org/project/tinytuya/)
  Install source: `pip install tinytuya`.
- [tinytuya Getting Started — DeepWiki](https://deepwiki.com/jasonacox/tinytuya/2-getting-started)
  Readable walkthrough of setup, the wizard, and device classes.
- ["How do I get the local_key?" — tinytuya Discussion #111](https://github.com/jasonacox/tinytuya/discussions/111)
  The canonical answer to the single hardest step. Use for: key-fetch troubleshooting.
- [Tuya IoT Platform](https://iot.tuya.com/)
  Where you create the free developer account the wizard authenticates against
  (the one-time cloud touch to read the local key).
- [Home Assistant — LocalTuya integration](https://github.com/xZetsubou/hass-localtuya)
  Alternative/validation path; good DP-discovery UI. Use for: cross-checking which
  data points (DPs) your bulb exposes.
- [Tuya local protocol notes — TuyAPI protocol docs](https://github.com/codetheweb/tuyapi/blob/master/docs/SETUP.md)
  Background on the encrypted LAN protocol (port 6668, AES, protocol versions).

## Knowledge — fully-offline key extraction (the chosen route)

- [Decode devices from a rooted device for Smart Life — udnaan gist](https://gist.github.com/udnaan/b3947a0dadf23bfd47ad54dd02e0ccef)
  **Primary source for Lesson 2.** On-phone file location for the local keys and the
  MMKV-vs-XML shift; comments track app-version changes. Use for: where the key lives.
- [HiveMindAutomation/LocalTuyaKeyExtractor](https://github.com/HiveMindAutomation/LocalTuyaKeyExtractor)
  and [MarkWattTech/TuyaKeyExtractor](https://github.com/MarkWattTech/TuyaKeyExtractor)
  Parse the app's `preferences_global_key` file into clean key lists. Use for: a
  reference parser if the regex needs hardening.
- [tuya-cli — TuyAPI](https://github.com/TuyaAPI/cli) and
  [redphx/tuya-local-key-extractor](https://github.com/redphx/tuya-local-key-extractor)
  Cloud/developer-API fetchers — the route we are NOT using; here for contrast.
- [tinytuya network scanner](https://github.com/jasonacox/tinytuya#network-scanner)
  scanner + notes on packet-capture (mitmproxy) approaches — the fragile fallback.

## Wisdom (Communities)

- [Home Assistant Brasil — Fórum](https://homeassistantbrasil.com.br/)
  PT-BR community with direct Intelbras/Izy/Tuya experience. Use for: device-specific
  quirks (e.g. EWS 410 protocol version, DP map). Search before asking.
- [r/homeassistant](https://reddit.com/r/homeassistant)
  Large, high-signal smart-home community; strong on LocalTuya.
- [tinytuya GitHub Discussions](https://github.com/jasonacox/tinytuya/discussions)
  Best place for tinytuya-specific issues, often answered by the maintainer.

## Gaps / to confirm against the real device
- Exact **protocol version** of this bulb's firmware (3.3 vs 3.4/3.5) — determines
  the control call. Resolve in Lesson 3 from a real `scan`.
- The bulb's **DP map** (which data point = power, mode, brightness, color, temp).
  Resolve empirically once local control is up.
