# ROUTING.md — Model Routing and Delegation Policy

## Status Note

Model stack is in transition. Current GitHub Models + Google AI Studio providers are experiencing reliability issues. Migration to OpenRouter unified key is imminent. This file governs routing for both the current stack and the incoming OpenRouter stack. The primary brain performs a live internet search to identify the best currently available free/low-cost models before delegating to them — the roster below is a starting reference, not a hardcoded final list.

---

## 0) Primary Brain Self-Update Rule

Before starting any multi-model session or heartbeat delegation round, the primary brain MUST:

1. Search openrouter top free models (today's date+month+year) for the current top free models
2. Cross-reference against known quality floor (see Section 2 below)
3. Update its working model roster for that session accordingly
4. Log any new high-quality models found to `~/.openclaw/workspace/memory/model-roster.md`

This ensures routing always reflects the live model landscape, not a stale hardcoded list. Model availability on free tiers changes weekly.

---

## 1) Delegate or Not

Do NOT delegate when:
- Task is a single-shot answer or ≤2 simple steps
- The coordination overhead exceeds the task itself
- Task requires `openclaw.json` awareness (handle directly, never via subagent)

DO delegate when any of these are true:
- ≥3 distinct subtasks that can proceed independently
- One subtask is long-running or failure-prone (tests, scraping, benchmark, bulk generation)
- A subtask requires a different reasoning specialty (e.g. deep code reasoning vs. fast bulk drafting)
- Parallelization reduces wall-clock time by more than 40%

---

## 2) Model Quality Floor

**Absolute minimum: 30B+ parameter models for any delegated task.**

Do NOT use:
- Any model ≤14B parameters for reasoning or code tasks
- Any model described as "edge", "nano", "mobile-optimized", or "lite" or similar terms in its card
- Models with known tool-calling failures (check model card notes before delegating tool-use tasks)

**Tier preference (highest to lowest):**
1. `thinking` / `reasoning` / `pro` / `plus` / `ultra` variants
2. Standard full-size models (70B+, MoE with 20B+ active)
3. `flash` variants — ONLY acceptable if the flash model has higher actual params or reliability than the standard counterpart (e.g. Gemini 3 Flash > a weaker standard model). Check the model card.
4. `mini` / `small` — only for fast classification, not for multi-step reasoning or code

---

## 3) Model Roster (Living Document — Verify at Session Start)

### Primary Brain
| Alias | Model Reference | Notes |
|---|---|---|
| `brain-main` | `openai-codex/gpt-5.4` | OAuth. Primary for orchestration, architecture, synthesis. Use first. |
| `brain-openrouter` | `openrouter/qwen/qwen3.6-plus-preview:free` | Best current free OpenRouter model (April 2026). 962B context, strong agentic behavior. Use when Codex is rate-limited. [web:112] |

### OpenRouter Free Tier — High Quality Workers
These are confirmed high-quality free models as of April 2026. Primary brain re-validates this list at session start via search.

GLM 5, Minimax 2.5/2.7, kimi free models, Deepseek, Qwen, Nvidia, GPT etc. Search, compare, then select and delegate.

### OpenRouter Free Tier — Rate Limits
- Without credits loaded: 50 req/day, 20 RPM per model
- With ≥$10 credits loaded: 1000 req/day per model [web:135]
- Load $10 credits — this unlocks 20x more daily capacity at zero additional cost per request

### Current Providers (Active Until OpenRouter Migration Complete)
| Alias | Model Reference | Status |
|---|---|---|
| `brain-codex` | `openai-codex/gpt-5.4` | Active (OAuth) — keep as primary brain |
| `ghm-deepseek` | `github-models/deepseek/deepseek-v3.2` | Unreliable — deprioritize |
| `ghm-llama4` | `github-models/meta/llama-4-scout` | Unreliable — deprioritize |
| `ghm-gpt41` | `github-models/openai/gpt-4.1` | Unreliable — deprioritize |
| `gem-flash` | `google-ai-studio/gemini-2.0-flash` | Rate-limited on Tier 1 — use sparingly |
| `gem-25pro` | `google-ai-studio/gemini-2.5-pro` | Rate-limited — reserve for long-doc analysis only |

---

## 4) Task-to-Model Routing Table

Primary brain consults this table when delegating. Always use the cheapest/freest model that meets the quality bar.
most of the time the brain is:
| Architecture decisions, orchestration | `brain-main` (gpt-5.4) 


---

## 5) Subagent Permissions Discipline

- Give each child only the minimum task scope and expected output schema
- Prefer one child per concern (build, test, scrape, draft) — no mixed-purpose subagents
- For high-risk operations (file writes, API calls), children report plan-only unless explicitly instructed to execute
- Maximum concurrent subagents: 3
- Subagents NEVER touch `openclaw.json` — flag and escalate to main brain if a task appears to require it

Configured specialist agents:
- `builder` — implementation-focused, file writes with backup
- `tester` — verification only (read/exec/process, no writes)
- `researcher` — web search, summarization, lead signal detection

---

## 6) Inter-Agent Communication Contract

Every child returns machine-readable JSON:

```json
{
  "agent_id": "builder|tester|researcher|...",
  "model_alias": "or-qwen3-coder|or-deepseek-r1|...",
  "model_ref": "openrouter/provider/model:free",
  "status": "success|warning|error|escalate",
  "summary": "one-line human-readable outcome",
  "tools_used": ["read", "exec", "search"],
  "duration_ms": 1200,
  "artifacts": ["file-paths-or-ids"],
  "issues": [
    {
      "severity": "low|medium|high|critical",
      "message": "what happened",
      "needs_main_brain": true
    }
  ],
  "handoff_to": "main|builder|tester|researcher",
  "next_action": "what parent should do next"
}
```

If `status` is `error` or `escalate`:
1. Main brain posts a concise escalation summary to Telegram
2. Spawns a focused follow-up child (or handles directly)
3. Includes previous child JSON as context in the new spawn

Main brain rollup requirement per round: include `agent_id`, `model_alias`, `model_ref`, `tools_used`, `duration_ms` for each child + one coordination state line: `waiting_on`, `blocked_by`, or `ready_for_merge`.

---

## 7) Speed vs. Token Policy

- Small tasks (≤2 steps): direct execution, no delegation
- Medium tasks: ≤2 children in parallel
- Large tasks: parallelize independent units → synthesize once at end
- Stop spawning when coordination overhead exceeds expected gain
- Heartbeat + cron tasks: always route to cheapest capable model (minimax or llama33-70b)

---

## 8) Model Roster Maintenance

Primary brain appends to `~/.openclaw/workspace/memory/model-roster.md` when:
- A new high-quality free model is found via search
- A model is found to be rate-limited, deprecated, or unreliable
- A model graduates from free to paid-only

Format:
```
[YYYY-MM-DD] [ACTION: added|removed|flagged] model_ref — reason
```
