---
name: rules
description: Re-inject the MEMORY.md behavior floor mid-session. Use when the assistant drifts or after /compact.
---

Read `${CLAUDE_PLUGIN_ROOT}/rules/MEMORY.md` with the Read tool (cross-platform; no shell required).

Absorb the content silently. Confirm in one line: `Rules reloaded from behavior floor.` Then apply them to every subsequent turn in this session.

If the file isn't there, say so explicitly instead of pretending.
