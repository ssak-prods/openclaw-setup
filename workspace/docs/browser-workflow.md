# Browser workflow (phases 1–3)

Implemented baseline for practical browsing:

## What it does
- Starts the isolated `private` OpenClaw browser profile
- Opens a URL
- Captures an interactive snapshot (`snapshot --interactive --json`)
- Extracts interactive refs and nav-like items
- Optionally clicks a chosen ref
- Tries to capture a screenshot and reports any screenshot timeout cleanly

## Script
`./scripts/browser_walk.py`

## Usage
```bash
./scripts/browser_walk.py https://example.com
./scripts/browser_walk.py --click-ref e1
./scripts/browser_walk.py https://www.reddit.com/r/python/
```

## Output shape
JSON with:
- `opened`
- `summary.url`
- `summary.interactive_count`
- `summary.items`
- `summary.nav_like`
- `summary.snapshot_text`
- `screenshot`
- `screenshot_error`

## Current scope
This covers the core first-pass workflow for:
1. open site
2. inspect visible links/buttons
3. identify useful navigation targets
4. click through selected targets
5. verify destination with another snapshot

## Add-ons later
- hover/type pacing
- visual analyst fallback
- richer multi-page trail/state
- installed skill augmentation (`playwright-mcp`)
