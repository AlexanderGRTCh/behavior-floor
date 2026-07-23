---
name: comms
description: Load a comms audience profile from the behavior floor. Usage - /comms [chat|docs|published-copy]. Default chat (skim-fast + teach-senior-engineer; bold verdict first, teaching in marked skippable lines).
---

Read the profile argument from the user. If empty or not one of `chat` / `docs` / `published-copy`, default to `chat`.

Read `${CLAUDE_PLUGIN_ROOT}/rules/comms/<profile>.md` via the Read tool (CORE.md is already auto-injected at session start; do not re-read it), absorb silently, then apply it to every relevant reply or drafted text for the rest of the session. For `chat`: lead with a bold verdict line, teaching in marked skippable lines (at most one per message), follow the four templates and the self-checklist.

Confirm in one line only:

```
Comms profile loaded - <profile> (rules/comms).
```

If a file is missing, say so explicitly and stop, do not invent a style.
