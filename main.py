#!/usr/bin/env python3
"""The Internet in One Word entry.

Writes one word to /output/entry.txt: "Receipts".

Pure standard library. Deterministic: the same word every run.
The gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
not only white space.
"""

import os
import sys

WORD = "Receipts"


def main() -> None:
    if not 1 <= len(WORD) <= 30 or not WORD.strip():
        raise SystemExit(
            f"word is {len(WORD)} characters, outside the 1-30 gate"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
