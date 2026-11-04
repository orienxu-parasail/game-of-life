#!/usr/bin/env python3
"""Command-line runner; test cases are in tests/test_part1.py, etc.

Part 1 can also be run directly: python3 -m unittest tests.test_part1 -v
"""

import sys

if sys.version_info < (3, 9):
    print("Python 3.9 or newer is required.", file=sys.stderr)
    sys.exit(2)

import os
from pathlib import Path
import subprocess


def main():
    root = Path(__file__).resolve().parent
    env = root / ".venv"
    python = env / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not (env / "pyvenv.cfg").is_file() or not python.is_file():
        print("Test environment is not ready. Run setup first:", file=sys.stderr)
        print("  python3 setup.py  (Windows: py -3 setup.py)", file=sys.stderr)
        return 2
    try:
        # Use the prepared interpreter even when launched by a different Python.
        return subprocess.call([str(python), "-E", str(root / "run_tests.py")] + sys.argv[1:],
                               cwd=str(root))
    except OSError as exc:
        print("Cannot start test environment: %s. Rerun setup for diagnostics." % exc,
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
