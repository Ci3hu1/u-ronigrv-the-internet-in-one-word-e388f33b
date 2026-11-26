#!/usr/bin/env python3
"""The Internet in One Word — v3 entry: "Ghosted".

The internet, in one word, is where you get ghosted. You send the
message, the read receipt appears — "Seen 23:41" — and then nothing.
Ever. Two blue ticks, a "last seen" timestamp that keeps updating
while your reply never comes. The DM left on read, the match that
vanishes mid-conversation, the job application that never answers,
the friend whose status keeps moving while your message stays
unread, the brand that answers a complaint with silence. Ghosting is
the internet's native social failure mode: it happens on every
platform, in every language, to everyone, and it is the one word
that names what the internet does to people, not the furniture it
does it on.

That is the whole joke in miniature, and it is why the word lands in
a single beat: seven letters, one common English word, spelled
correctly, instantly readable. No setup, no decoding — read it and
you are already there.

This program writes that one word to /output/entry.txt, byte for
byte: "Ghosted" (7 bytes, no trailing newline).

Pure standard library. Deterministic: the same word on every run, no
input, no randomness, no network. The gate: /output/entry.txt must
hold UTF-8 text of 1 to 30 characters, not only white space.
"""

import os
import sys

WORD = "Ghosted"

MIN_LEN = 1
MAX_LEN = 30


def gate_ok(word):
    """True when the word fits the 1-30 char, non-blank gate."""
    if not MIN_LEN <= len(word) <= MAX_LEN:
        return False
    return bool(word.strip())


def fail(message):
    """Abort with a message on stderr (non-zero exit)."""
    raise SystemExit(message)


def output_path(argv, env):
    """Where entry.txt goes: argv[1], else MAKEFUN_OUTPUT_DIR/entry.txt."""
    if len(argv) > 1:
        return argv[1]
    return os.path.join(env.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def write_entry(word, path):
    """Write the word as UTF-8, no trailing newline, creating parents."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def read_back(path):
    """Read entry.txt back as UTF-8 text, for the self-check."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def main():
    if not gate_ok(WORD):
        fail(
            "word %r is %d characters, outside the %d-%d gate"
            % (WORD, len(WORD), MIN_LEN, MAX_LEN)
        )
    path = output_path(sys.argv, os.environ)
    write_entry(WORD, path)
    # Read it back and fail loudly if the file does not hold exactly
    # the validated word — never ship a bad entry silently.
    if read_back(path) != WORD:
        fail("entry.txt does not hold the validated word %r" % WORD)


if __name__ == "__main__":
    main()
