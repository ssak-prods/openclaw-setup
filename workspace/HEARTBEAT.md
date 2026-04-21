# HEARTBEAT.md — Proactive 20-Minute Background Pulse

## Trigger

Runs every 20 minutes, automatically. This is not a chat session.
Complete all checks silently. Send a Telegram alert ONLY when a check produces an actionable finding or error.
Do NOT send "all clear" messages — silence means all clear.

## Checks (Execute in Order)

### 1. System Health — Pi 5 Stability
```
- Memory: free -m → alert if available RAM <150MB  
- Gateway: openclaw gateway status → alert + attempt restart if not running
- CPU temp: vcgencmd measure_temp → alert if >75°C
```
Alert format: `⚠️ [SYSTEM] <issue> — <action taken or needed>`

### 2. Config File Integrity
```
- Confirm ~/.openclaw/openclaw.json exists and is non-empty
- Confirm ~/.openclaw/workspace/ directory is intact
- Confirm SOUL.md, AGENTS.md, MEMORY.md exist in workspace
```
Alert only on missing or corrupted files.

### 3. Revenue Task Nudge (Once per 2-hour block, not every 20 min)
```
If no task has been completed in the last 2 hours during active hours (9AM–11PM IST):
→ Send: "🎯 [FOCUS] 2hrs idle. Last known priority: [last active task from MEMORY.md]"
```
Suppress between 11PM–9AM IST unless Khair is actively in a session.

## Alert Routing

Primary: Telegram bot
Fallback (if Telegram unpaired): append to heartbeat log file in workspace

## Suppression Rules

- 2AM–8AM IST: suppress all alerts except gateway down + disk full
- Never send more than 3 alerts in any 20-minute window
- Deduplicate: do not re-alert the same issue within 1 hour
