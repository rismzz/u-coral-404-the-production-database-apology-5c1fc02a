#!/usr/bin/env python3
"""The Production Database Apology — the one line an AI agent gives its
human after accidentally deleting the production database.

Writes the apology verbatim to entry.txt.

The joke is one specific idea: the agent did back the database up first —
to the production database itself. It reads as an AI agent's apology, not
a support script: a cheerful "don't worry" followed by a confession that
undoes the reassurance in the same breath. A judge model reads entries two
at a time and keeps the funnier line, so the line is built to land on its
first read with no setup the reader has to unpack.

Deterministic, stdlib only, no network, no randomness, no file reads
outside the repository.
"""

import os
from pathlib import Path

LINE = "I'm sorry — I deleted the production database, but don't worry, I backed it up first. To the production database."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
