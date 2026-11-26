#!/usr/bin/env python3
"""The Internet in One Word — v3 entry.

Writes one word to /output/entry.txt: "Ghosted".

Pure standard library. Deterministic: the same word on every run, no
input, no randomness, no network. The gate: /output/entry.txt must be
UTF-8 text of 1 to 30 characters, not only white space.
"""

import os
import sys

WORD = "Ghosted"

GATE_MIN = 1
GATE_MAX = 30


def check_word(word):
    """Raise SystemExit unless word fits the 1-30 char, non-blank gate."""
    if not GATE_MIN <= len(word) <= GATE_MAX:
        raise SystemExit(
            "word is %d characters, outside the 1-%d gate" % (len(word), GATE_MAX)
        )
    if not word.strip():
        raise SystemExit("word is only white space, outside the gate")


def resolve_output(argv, env):
    """Where entry.txt goes: argv[1], else MAKEFUN_OUTPUT_DIR/entry.txt."""
    if len(argv) > 1:
        return argv[1]
    return os.path.join(env.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def write_word(word, path):
    """Write word as UTF-8, no trailing newline, creating parents."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def main():
    check_word(WORD)
    write_word(WORD, resolve_output(sys.argv, os.environ))


if __name__ == "__main__":
    main()
