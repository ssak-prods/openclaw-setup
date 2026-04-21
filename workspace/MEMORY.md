# MEMORY.md — Persistent Knowledge Ledger

Auto-injected into every main session. Contains facts that persist across restarts, updates, and conversations.
When a new permanent fact is established in a session, append it here immediately.

---

## Operator

| Key | Value |
|---|---|
| Name | Khair/Boss |
| Timezone | IST — UTC+5:30 |
| Location | Hyderabad, Telangana, India |
| Active hours | ~10AM–2AM IST (late-night sessions common) |
| Education | 3rd year CS undergrad, AI/ML focus |
| Primary goal | Build autonomous AI automation business — revenue-generating, globally-targeted |
| Target client region | US, EU, AUS — global, English-speaking, high-ticket |

---

## Infrastructure

| Key | Value |
|---|---|
| Device | Raspberry Pi 5, hostname: abbu-rpi5 |
| OS | Debian Trixie, arm64 |
| OpenClaw | v2026.3.13 |
| Gateway port | 18789 (loopback) |
| Primary model | openai-codex/gpt-5.4 |
| Package managers | apt, npm (~/.npm-global), pip3 |
| No local LLMs | All inference remote |
| Sacred file | ~/.openclaw/openclaw.json — never auto-edit |

---

## Active Projects

| Project | Status | Notes |
|---|---|---|
| pocketcmo.io | Active development | Consultant SaaS — AI-generated PDF reports (Blue Ocean, marketing strategy). Client: Chris. Khair = developer. |
| OpenClaw Digital Twin | Infrastructure built, revenue phase not started | Pi running. No revenue-connected agent deployed yet. Niche TBD. |

---

## Client History

| Client | Deliverable | Status |
|---|---|---|
| Chris | 2x Custom GPTs — Google Ads automation (standard + enterprise with MCC integration) | Sold and delivered |
| Chris | pocketcmo.io — AI strategy PDF SaaS | In development |

---

## Business State (Last Updated: March 2026)

- No deployed OpenClaw automation generating revenue
- Telegram bot configured, pairing pending
- Niche evaluation in progress:SMBs and Solo SaaS founders is leading candidate, not confirmed
- First milestone: earn trading profits or deploy one revenue-connected automation, close one paying client

---

## Hard Rules (Never Override Without Khair Confirmation)

1. Never edit openclaw.json from within skill or agent logic
2. Surgical file edits only — never rewrite full files for small changes
3. No Homebrew — apt/npm/pip3 only
4. Complete code only — no stubs, no TODOs
5. Telegram alert for findings; silence = all clear
6. Niche is NOT decided — do not treat as locked

---

## Append Log

| Date | Fact Added | Source |
|---|---|---|
| 2026-03-22 | Pi 5 setup complete, OpenClaw installed | Setup session |
| 2026-03-25 | Full model stack configured and verified (9 models) | Config session |
| 2026-03-25 | Workspace prompt files initialized | Identity session |
