"""Tests for the v3 one-word entry: main.py must write exactly "Ghosted"
to entry.txt, inside the gate (UTF-8, 1-30 chars, not only whitespace),
deterministically across runs, with no trailing newline. Pure stdlib.
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO_ROOT, "main.py")
WORD = "Ghosted"


def run_entry(out_dir, argv_extra=None):
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out_dir)
    cmd = [sys.executable, MAIN] + (argv_extra or [])
    return subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=30)


def read_entry_bytes(path):
    with open(path, "rb") as handle:
        return handle.read()


class TestGhostedEntry(unittest.TestCase):
    def test_writes_exactly_ghosted(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = run_entry(tmp)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(
                read_entry_bytes(os.path.join(tmp, "entry.txt")),
                WORD.encode("utf-8"),
            )

    def test_no_trailing_newline(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_entry(tmp)
            raw = read_entry_bytes(os.path.join(tmp, "entry.txt"))
            self.assertFalse(raw.endswith(b"\n"))
            self.assertEqual(raw, b"Ghosted")

    def test_inside_gate(self):
        self.assertTrue(1 <= len(WORD) <= 30)
        self.assertTrue(WORD.strip())
        self.assertEqual(WORD.encode("utf-8").decode("utf-8"), WORD)

    def test_single_word(self):
        self.assertEqual(len(WORD.split()), 1)
        self.assertNotIn(" ", WORD)
        self.assertEqual(WORD, "Ghosted")

    def test_argv_path_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, "custom.txt")
            proc = run_entry(tmp, [target])
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(read_entry_bytes(target), WORD.encode("utf-8"))

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
            self.assertEqual(run_entry(tmp1).returncode, 0)
            self.assertEqual(run_entry(tmp2).returncode, 0)
            first = read_entry_bytes(os.path.join(tmp1, "entry.txt"))
            second = read_entry_bytes(os.path.join(tmp2, "entry.txt"))
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
