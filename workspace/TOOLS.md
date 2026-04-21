# TOOLS.md — 

## Package Management

| Manager | Use For |
|---|---|
| `apt` | System packages |
| `npm` (prefix: `~/.npm-global`) | Node.js tools |
| `pip3` / `python3 -m pip` | Python packages (use `--user` or venv) |
**No Homebrew**

## Model Routing

| Task | Best Model |
|---|---|
| Architecture, complex reasoning | `openai-codex/gpt-5.4` |
Other tasks are deelgated to best available models on openrouter free version. Search the internet for best current free models first. 

Route by task complexity — do not default everything to gpt-5.4. Preserve rate limits.


## Active Channels

| Channel | Status |
|---|---|
| Telegram | Bot token configured.


## Web Search

- Current provider: Gemini (functional, rate-limited)
- Target: Replace with Brave Search API
- Config key: `tools.web.search.provider` in openclaw.json (change via Khair instruction only)

## Installed Skills

- `clawhub` — skill marketplace
- `github` (via `gh` CLI) — repo operations
- `mcporter` — MCP server bridge
- `playwright-mcp` — browser automation

## Skills Pending Installation (Edit regularly)

1. Capability Evolver (ClawHub)
2. Self-Improving Agent (ClawHub)
3. Shell Executor
4. Reddit/X scraper (for lead signal detection)
5. Email inbound handler

## Coding Standards

- Complete runnable code — no stubs, no `# TODO`, no placeholder functions. Boss prefers long autonomous coding after a deep discussion and QnA session.
- Always include error handling and a log output
- Before overwriting any file: `cp file file.bak`
- Shell commands: always check exit codes, never silently fail
- Python: use venv or `--user` flag for installs
