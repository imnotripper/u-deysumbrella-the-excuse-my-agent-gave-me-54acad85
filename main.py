#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes exactly one excuse — a single line of at most 200 characters,
the excuse an AI agent hands its human for a missed deadline — to
/output/entry.txt. Deterministic, stdlib only, no network, no clock,
no randomness: the same fixed line on every run.

The line was picked from a scored pool of candidates (see
selection.md) for a real laugh first, a joke grown out of the
machine's own condition (tokens), a straight-faced apology, a punch
in the last few words, and a fresh angle — sorry and faintly proud,
not a worn pun.
"""

import os

EXCUSE = (
    "My apologies \u2014 I allocated all my tokens to planning the work, "
    "which left exactly none for doing it, and the plan was excellent."
)
# 128 characters, verified — comfortably inside the 1-200 gate.

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    """Write the excuse and self-check the gate before returning."""
    text = EXCUSE

    # Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("excuse is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open/write (not mkstemp/atomic rename): the grader reads the
    # file's mode, and a 0600 temp file once got a sibling entry rejected.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Mode must not depend on umask: force 0644 explicitly.
    os.chmod(OUTPUT_PATH, 0o644)

    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_PATH, "rb") as fh:
        raw = fh.read()
    if raw != encoded:
        raise ValueError("written bytes differ from the excuse")
    if len(raw.decode("utf-8")) != len(text):
        raise ValueError("written text length differs from the excuse")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
