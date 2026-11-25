#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one line of text (a roast of a smart fridge that refuses to open
after midnight) to /output/entry.txt.

Angle: the fridge as a petty librarian — a fresh trope, no bouncer /
curfew / restraining-order / Do-Not-Disturb cliche. The turn is the
little "Shhh" sign: the leftovers are asleep, and so should you be.
"""

import hashlib
import os
import sys

ENTRY = (
    "At midnight my fridge goes librarian \u2014 lights off, door locked, "
    "and a little sign: 'Shhh. The leftovers are sleeping, and frankly, "
    "so should you.'"
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry against the gate: UTF-8, 1-200 chars, not only whitespace.

    Returns (ok, errors): ok is True when the entry passes every check.
    """
    errors = []
    if not isinstance(text, str):
        return False, ["entry is not a string"]
    if text != text.strip():
        errors.append("entry has leading or trailing whitespace")
    if not text.strip():
        errors.append("entry is empty or only whitespace")
    if len(text) < 1:
        errors.append("entry is shorter than 1 character")
    if len(text) > 200:
        errors.append("entry is longer than 200 characters (%d)" % len(text))
    if "\n" in text or "\r" in text:
        errors.append("entry must be a single line (no newline characters)")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        errors.append("entry is not valid UTF-8: %s" % exc)
    return (not errors), errors


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        for err in errors:
            print("validate failed: %s" % err, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Guard: what landed on disk must be byte-identical to ENTRY.
    with open(OUTPUT_PATH, "rb") as f:
        on_disk = f.read()
    if on_disk != ENTRY.encode("utf-8"):
        print("verify failed: /output/entry.txt does not match ENTRY",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(on_disk).hexdigest()
    print("wrote %s (%d chars) sha256=%s" % (OUTPUT_PATH, len(ENTRY), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
