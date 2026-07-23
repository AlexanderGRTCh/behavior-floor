#!/usr/bin/env python
"""inject_floor.py - cross-platform Claude Code hook helper for the behavior floor.

Emits the always-on rules-floor context to stdout so Claude Code injects it into
the model's context. Wired from hooks/hooks.json:

    python inject_floor.py session-start   # MEMORY.md + comms/CORE.md
    python inject_floor.py digest          # comms/DIGEST.md

Path resolution (no hard-coded absolute path):
  1. the FLOOR_ROOT environment variable, if set, then
  2. the plugin root inferred from this file's location
     (<plugin_root>/hooks/inject_floor.py -> <plugin_root>).

Exit code is always 0: a missing rules file emits a short placeholder note rather
than failing the hook, so a partial install never blocks a session from starting.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _rules_dir() -> Path:
    """Locate <floor_root>/rules without hard-coding any absolute path."""
    env = os.environ.get("FLOOR_ROOT")
    if env:
        return Path(env).expanduser() / "rules"
    # <plugin_root>/hooks/inject_floor.py -> <plugin_root>
    return Path(__file__).resolve().parent.parent / "rules"


def _force_utf8_stdout() -> None:
    """Rule files use non-ASCII glyphs; a cp1252/legacy console would crash on print."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Python 3.7+
    except Exception:
        pass


def _emit(title: str, path: Path) -> None:
    print(f"=== {title} ===")
    try:
        print(path.read_text(encoding="utf-8"))
    except OSError:
        print(f"[{path.name} not found]")
    print()


def main(argv: "list[str]") -> int:
    _force_utf8_stdout()
    mode = argv[1] if len(argv) > 1 else "session-start"
    rules = _rules_dir()
    if mode == "digest":
        _emit("comms DIGEST", rules / "comms" / "DIGEST.md")
    else:  # session-start
        _emit("MEMORY.md (always-on rules)", rules / "MEMORY.md")
        _emit("comms CORE.md (always-on comms invariants)", rules / "comms" / "CORE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
