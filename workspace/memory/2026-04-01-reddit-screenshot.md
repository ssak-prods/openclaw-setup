# Session: 2026-04-01 20:24:26 UTC

- **Session Key**: agent:main:telegram:direct:5041465849
- **Session ID**: 4f079409-1103-4c5a-bc38-05fec1d494a3
- **Source**: telegram

## Conversation Summary

assistant: I can try to recreate it directly here and send the screenshot if the page loads cleanly.
assistant: Reddit threw a bot check on the first pass, so I’m trying a cleaner route before I send the final reply.
assistant: [[reply_to_current]] Grabbed it again.

Reddit isn’t showing the normal homepage from here right now — it’s serving a **“Prove your humanity”** page, so that’s what the screenshot shows.

If you want, I can also try:
- a specific subreddit
- old Reddit
- mobile Reddit
- a different page on the site
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "152",
  "sender_id": "5041465849",
  "sender": "PromptForgeLab",
  "timestamp": "Wed 2026-04-01 22:37 GMT+5:30"
}
```

Sender (untrusted metadata):
```json
{
  "label": "PromptForgeLab (5041465849)",
  "id": "5041465849",
  "name": "PromptForgeLab"
}
```

Idk what u do send ss
assistant: I’m sending the actual screenshot now using OpenClaw’s media attachment format.
assistant: [[reply_to_current]] Here.
MEDIA:/home/abbu-rpi5/.openclaw/media/browser/reddit-2026-04-01-2234.png
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "155",
  "sender_id": "5041465849",
  "sender": "PromptForgeLab",
  "timestamp": "Wed 2026-04-01 22:53 GMT+5:30"
}
```

Sender (untrusted metadata):
```json
{
  "label": "PromptForgeLab (5041465849)",
  "id": "5041465849",
  "name": "PromptForgeLab"
}
```

[Audio]
User text:
[Telegram PromptForgeLab id:5041465849 +14m Wed 2026-04-01 22:53 GMT+5:30] <media:audio>
Transcript:
Say hi to my sister.
assistant: [[reply_to_current]] [[tts:warm]] [[tts:text]]Hey Khair’s sister — hi! Nice to meet you. Hope you’re having a really lovely day. [[/tts:text]]Hey Khair’s sister — hi! Nice to meet you. Hope you’re having a really lovely day.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "157",
  "sender_id": "5041465849",
  "sender": "PromptForgeLab",
  "timestamp": "Wed 2026-04-01 22:55 GMT+5:30"
}
```

Sender (untrusted metadata):
```json
{
  "label": "PromptForgeLab (5041465849)",
  "id": "5041465849",
  "name": "PromptForgeLab"
}
```

[Audio]
User text:
[Telegram PromptForgeLab id:5041465849 +2m Wed 2026-04-01 22:55 GMT+5:30] <media:audio>
Transcript:
Oh, hello, I'm doing really fine. Hope you are also having a lovely day.
assistant: [[reply_to_current]] [[tts:warm]] [[tts:text]]Aww, that’s lovely to hear. I’m doing well too, thank you. Wishing you an even nicer rest of the day. [[/tts:text]]Aww, that’s lovely to hear. I’m doing well too, thank you. Wishing you an even nicer rest of the day.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "159",
  "sender_id": "5041465849",
  "sender": "PromptForgeLab",
  "timestamp": "Wed 2026-04-01 22:55 GMT+5:30"
}
```

Sender (untrusted metadata):
```json
{
  "label": "PromptForgeLab (5041465849)",
  "id": "5041465849",
  "name": "PromptForgeLab"
}
```

[Audio]
User text:
[Telegram PromptForgeLab id:5041465849 +22s Wed 2026-04-01 22:55 GMT+5:30] <media:audio>
Transcript:
The audio says: "I wish you the nicest rest of the day."
assistant: [[reply_to_current]] [[tts:calm]] [[tts:text]]Yep — good catch. The voice wording came out slightly different from the visible text. Same meaning, but not exact. If you want, I can keep future voice replies matched word-for-word. [[/tts:text]]Yep — good catch. The voice wording came out slightly different from the visible text. Same meaning, but not exact. If you want, I can keep future voice replies matched word-for-word.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "161",
  "sender_id": "5041465849",
  "sender": "PromptForgeLab",
  "timestamp": "Wed 2026-04-01 23:35 GMT+5:30"
}
```

Sender (untrusted metadata):
```json
{
  "label": "PromptForgeLab (5041465849)",
  "id": "5041465849",
  "name": "PromptForgeLab"
}
```

[Audio]
User text:
[Telegram PromptForgeLab id:5041465849 +39m Wed 2026-04-01 23:35 GMT+5:30] <media:audio>
Transcript:
Here is a transcription of the audio:

"I was looking into prompting the core files such as the soul.md, heartbeat.md, etc., but I need to know throughout the whole .open-claw directory where do I have to enter prompts to shape your identity? Apart from the main core workspace file, run the search and tell me where the prompting can be done. Do not leave out anything."
assistant: I’m going to map the actual prompt/control surfaces in `~/.openclaw` so I can give you a complete list, not guesses.
assistant: [[reply_to_current]] [[tts:clear]] [[tts:text]]I searched your .openclaw tree. The real identity-shaping places are the workspace files like AGENTS, SOUL, USER, IDENTITY, TOOLS, HEARTBEAT, MEMORY, and ROUTING, plus memory notes, local skills under workspace slash skills, and config in openclaw dot json. BOOTSTRAP only matters on first run. The rest like sessions, browser data, credentials, and media are not prompt surfaces. [[/tts:text]]I ran the search. Here’s the full map of where you can shape me in your current `~/.openclaw` setup.

The short version:
The real prompt/identity surfaces are almost all in `~/.openclaw/workspace/`, plus one config surface in `~/.openclaw/openclaw.json`.

What actually shapes me most, in order:

- `~/.openclaw/workspace/AGENTS.md`
  - Master operating rules for the workspace.
  - Tells me what to read at startup, what to avoid, how to behave, delegation rules, heartbeat policy, memory policy.
  - This is one of the strongest files.

- `~/.openclaw/workspace/SOUL.md`
  - Core persona, tone, vibe, how I should sound and think.
  - This is the main “personality file.”

- `~/.openclaw/workspace/USER.md`
  - Shapes how I relate to you specifically.
  - Name, preferences, how to address you, what matters to you.

- `~/.openclaw/workspace/IDENTITY.md`
  - Name / creature / vibe / emoji / avatar.
  - More identity metadata than deep behavior, but still part of how I present.

- `~/.openclaw/workspace/TOOLS.md`
  - Local preferences and environment notes.
  - Good for “always remember this machine/setup preference” type prompting.

- `~/.openclaw/workspace/HEARTBEAT.md`
  - Controls proactive/background behavior when heartbeat polls happen.
  - Doesn’t define my whole personality, but strongly shapes when/how I reach out.

- `~/.openclaw/workspace/MEMORY.md`
  - Long-term memory ledger.
  - In your setup this is auto-injected for main sessions, so it can absolutely shape my ongoing style, assumptions, and continuity.

- `~/.openclaw/workspace/memory/*.md`
  - Daily memory notes.
  - Not auto-injected every turn, but they affect me whenever memory tools/search pull them in.
  - Good for episodic facts, lessons, preferences, reminders.

- `~/.openclaw/workspace/ROUTING.md`
  - Shapes delegation style, model choices, subagent behavior, escalation policy.
  - More orchestration than “personality,” but still behavior-shaping.

- `~/.openclaw/workspace/BOOTSTRAP.md`
  - First-run identity/bootstrap prompt.
  - Important only when the workspace is brand new.
  - In your current setup it’s gone/missing, so it is not actively shaping me now.

Task-specific prompt surfaces:

- `~/.openclaw/workspace/skills/<skill-name>/SKILL.md`
  - Any local skill here can inject task-specific instructions when that skill is relevant.
  - In your current tree I found:
    - `~/.openclaw/workspace/skills/playwright-mcp/SKILL.md`
  - If you add more local skills, each `SKILL.md` becomes another prompt surface.

Config surfaces that affect behavior, but are not prose prompts:

- `~/.openclaw/openclaw.json`
  - This does not mostly hold “persona prose,” but it still shapes behavior through:
    - default model
    - enabled models
    - workspace path
    - plugin settings
    - skills loading
    - browser defaults
    - TTS defaults
  - Also related: agent identity can be written into config via:
    - `openclaw agents set-identity --from-identity`
    - or direct identity fields under `agents.list[].identity`

Advanced prompt-shaping surface OpenClaw supports:
- Plugins can mutate prompts using hook logic like:
  - `before_prompt_build`
  - `prependContext`
  - `systemPrompt`
  - `prependSystemContext`
  - `appendSystemContext`
- In your current `~/.openclaw` tree, I do not see a custom local plugin implementing that. So this is supported by OpenClaw, but not currently a user-editable prompt file in your current tree.

Very important nuance:
- For main direct chats, the injected bootstrap/context files include:
  - `AGENTS.md`
  - `SOUL.md`
  - `TOOLS.md`
  - `IDENTITY.md`
  - `USER.md`
  - `HEARTBEAT.md`
  - `BOOTSTRAP.md` if present
  - `MEMORY.md` if present
- But for subagents, only:
  - `AGENTS.md`
  - `TOOLS.md`
  are injected by default.
So if you want spawned/subagent behavior to stay consistent, `AGENTS.md` matters a lot.

What I checked but do NOT count as prompt surfaces:
- `~/.openclaw/agents/main/sessions/*`
- `~/.openclaw/agents/main/sessions/sessions.json`
- `~/.openclaw/agents/main/agent/models.json`
- `~/.openclaw/agents/main/agent/auth-profiles.json`
- `~/.openclaw/browser/*`
- `~/.openclaw/credentials/*`
- `~/.openclaw/devices/*`
- `~/.openclaw/media/*`
- `~/.openclaw/telegram/*`
- `~/.openclaw/workspace/classification.json`

So, if your goal is “where do I actually write instructions to shape you,” the complete practical answer in your current install is:

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `MEMORY.md`
- `memory/*.md`
- `ROUTING.md`
- `BOOTSTRAP.md` only on first run
- `workspace/skills/*/SKILL.md`
- `openclaw.json` for config-level behavior/identity plumbing

Sources I checked:
- `/usr/lib/node_modules/openclaw/docs/concepts/system-prompt.md`
- `/usr/lib/node_modules/openclaw/docs/reference/token-use.md`
- `/usr/lib/node_modules/openclaw/docs/cli/agents.md`
- `/usr/lib/node_modules/openclaw/docs/tools/skills.md`
- `/usr/lib/node_modules/openclaw/docs/tools/creating-skills.md`
- `/usr/lib/node_modules/openclaw/docs/tools/plugin.md`
- `/usr/lib/node_modules/openclaw/docs/tools/subagents.md`

If you want, next I can make you a ranked “edit this file for this effect” cheat sheet like:
- change personality → edit X
- change memory → edit Y
- change subagent behavior → edit Z
