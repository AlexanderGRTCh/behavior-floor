---
name: floor
description: Load persona + delegation context from the behavior floor. MEMORY.md + comms CORE.md are NOT re-read (auto-injected at session start; use /rules after drift).
argument-hint: [lite|full]
---

# floor loader

Load protocol context (persona, delegation doctrine) from the behavior-floor repo. `MEMORY.md` and `comms/CORE.md` are already auto-injected by the SessionStart hook; never re-read them here (token discipline; `/rules` exists for drift recovery).

## Tier selection

Read `$ARGUMENTS`. If empty or not `lite` / `full`, default to `lite`.

## File list per tier (read in parallel via the Read tool)

### `lite` (default)
- `${CLAUDE_PLUGIN_ROOT}/templates/persona/SOUL.md`
- `${CLAUDE_PLUGIN_ROOT}/templates/persona/IDENTITY.md`
- `${CLAUDE_PLUGIN_ROOT}/templates/persona/USER.md`

### `full`, lite plus:
- `${CLAUDE_PLUGIN_ROOT}/rules/CONTEXT.md`
- `${CLAUDE_PLUGIN_ROOT}/rules/AGENT_TEMPLATE.md`

## After reading

1. Absorb silently; do NOT echo file contents. Apply for the rest of the session.
2. Confirm in ONE line only:

```
floor context loaded - tier=<X>, <N> files loaded.
```

3. If any read failed, list failures on a separate line and proceed with what loaded.
