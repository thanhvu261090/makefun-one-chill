"""One Line, One Chill — make.fun bounty entry.

Writes a single sentence of horror to /output/entry.txt.
The line must pass the gate: UTF-8 text, 1-200 characters,
not only whitespace, a single line.
"""

import os
import sys

ENTRY = (
    "My daughter's drawing of our family shows four people, "
    "and tonight I counted only three of us at the dinner table."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Mirror the competition gate for the entry text."""
    if not isinstance(text, str):
        return False
    if text.strip() == "":
        return False
    if len(text) < 1 or len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        print("gate check failed", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the round trip: what landed on disk must be the entry,
    # byte for byte, with no added newline or re-encoding.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY or not gate_check(written):
        print("round-trip verification failed", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
