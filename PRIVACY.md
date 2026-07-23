# Privacy Policy — Behavior Floor

Effective 2026-07-22.

The Behavior Floor plugin collects no data. Specifically:

- **No network calls.** The plugin's hook script runs locally, reads only the rule files inside its own plugin directory, and writes its output to standard output for Claude Code to consume. It contains no HTTP client, no analytics, and no telemetry of any kind.
- **No data collection or storage.** The plugin does not read, store, or transmit your prompts, code, files, credentials, or any personal information.
- **No third-party services.** Nothing is shared with anyone, including us. We have no way of knowing you installed it.

The plugin is plain-text Markdown and one standard-library Python script; you can audit every line at https://github.com/AlexanderGRTCh/behavior-floor.

Claude Code itself is governed by Anthropic's own privacy policy; this document covers only what this plugin adds, which is nothing.

Questions: open an issue on the repository.
