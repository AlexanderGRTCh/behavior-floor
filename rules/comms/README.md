# rules/comms — Global Communications (brain-agnostic)

Single home for every rule about how the system communicates. Plain markdown, zero vendor config; any runtime (Claude Code CLI, Codex CLI, other) injects these files, never copies them.

## Layout

```
CORE.md             invariants + audience routing table; injected at every session start
DIGEST.md           short style digest injected at recency every turn (drift fix); body only, no header
chat.md             replies to the primary user; skim-fast + teach-senior-engineer (teaching mandatory on coding work)
published-copy.md   public persona copy (social, forums, video, image platforms)
docs.md             authored documents: plain guides, reports, docx pipeline
```

Additional audience profiles (outside email, investor or backer updates) follow the same pattern and ship as a v2 extension: add a profile file plus one routing row in CORE.md.

## Adapters (how each runtime injects)

- **Claude Code CLI:** SessionStart hook reads CORE.md alongside `{FLOOR_ROOT}/rules/MEMORY.md` (fires on startup, resume, AND compact; no matcher); UserPromptSubmit hook reads DIGEST.md every turn at recency; `/comms [profile]` loads a profile mid-session (default chat).
- **Any other runtime:** inject CORE.md into the session preamble (startup include, system prompt append, or read `{FLOOR_ROOT}/rules/comms/CORE.md`); expose one command that reads `{FLOOR_ROOT}/rules/comms/<profile>.md` on demand; inject DIGEST.md per turn if the runtime supports it, else rely on CORE.

## Maintenance

Edit rules here only. Harness files (hooks, slash commands, runtime includes) may only point to these paths. New audience = new profile file + one row in CORE.md's routing table.
DIGEST.md is a derived artifact of CORE.md's skim contract: regenerate it whenever CORE changes; keep it body-only (no header, every byte is injected every turn).
