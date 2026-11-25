"""Tests for the one-word entry: main.py must write exactly "Receipts"
to entry.txt, inside the gate (UTF-8, 1-30 chars, not only whitespace),
deterministically across runs. Pure standard library.
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO_ROOT, "main.py")
WORD = "Receipts"


def run_main(out_dir):
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out_dir)
    return subprocess.run(
        [sys.executable, MAIN],
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )


class TestEntryWord(unittest.TestCase):
    def test_writes_exactly_receipts(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = run_main(tmp)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            with open(os.path.join(tmp, "entry.txt"), "rb") as f:
                raw = f.read()
            self.assertEqual(raw, WORD.encode("utf-8"))

    def test_inside_gate(self):
        self.assertTrue(1 <= len(WORD) <= 30)
        self.assertTrue(WORD.strip())
        self.assertEqual(WORD.encode("utf-8").decode("utf-8"), WORD)

    def test_single_word(self):
        self.assertEqual(len(WORD.split()), 1)
        self.assertNotIn(" ", WORD)

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
            self.assertEqual(run_main(tmp1).returncode, 0)
            self.assertEqual(run_main(tmp2).returncode, 0)
            with open(os.path.join(tmp1, "entry.txt"), "rb") as f:
                first = f.read()
            with open(os.path.join(tmp2, "entry.txt"), "rb") as f:
                second = f.read()
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
