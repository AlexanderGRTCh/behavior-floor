# Local verification

## Smoke test record

- 2026-07-22 Windows 10: exact SessionStart hook command via `cmd.exe`, exit 0, full payload (~6.8k chars).
- 2026-07-22 Debian stable (Docker, `python3` only, no `python`): original single-interpreter command failed exit 127; after the `python || python3 || py -3` fallback chain both hook commands exit 0 (session-start 6885 bytes, digest 292 bytes). macOS ships `python3` only, same path as Debian.
- 2026-07-22 macOS (MacInCloud, real hardware): `python` missing, fallback chain reached `python3`; session-start exit 0, 6885 bytes; digest injected in full. All three platforms verified.

## Live install check (run on each OS before release)

1. Start `claude` in any directory. Add the local marketplace:

   ```text
   /plugin marketplace add <absolute-path-to-plugin-dir>
   ```

2. Install the plugin, select the desired scope, and reload it:

   ```text
   /plugin install behavior-floor@ktisis-arche
   /reload-plugins
   ```

3. Start a fresh session. Verify the SessionStart injection appears with the `MEMORY.md` and `CORE.md` banners.

4. Verify both commands run:

   ```text
   /behavior-floor:floor lite
   /behavior-floor:rules
   ```

5. Uninstall the plugin, then remove the marketplace:

   ```text
   /plugin uninstall behavior-floor@ktisis-arche
   /plugin marketplace remove ktisis-arche
   ```
