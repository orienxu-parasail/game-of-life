#!/usr/bin/env python3
"""Run the tests up to the requested part; cases live in tests/test_partN.py.

Only Part 1 is open at the start. Later parts are sealed in locked/ and are
opened one at a time: when every test up to the highest open part passes, the
next part's prompt, stub and tests are written into the folder.
"""

import argparse
import base64
import json
from pathlib import Path
import sys
import unittest
import zlib

ROOT = Path(__file__).resolve().parent
LOCKED = ROOT / "locked"
LAST_PART = 4


def is_open(part):
    return (ROOT / "tests" / ("test_part%d.py" % part)).is_file()


def highest_open_part():
    part = 1
    while part < LAST_PART and is_open(part + 1):
        part += 1
    return part


def unseal(part):
    """Write Part `part`'s files from locked/. Never overwrites an existing file."""
    sealed = LOCKED / ("part%d.sealed" % part)
    if not sealed.is_file():
        return []
    body = sealed.read_text(encoding="utf-8").split("\n", 1)[1]
    files = json.loads(zlib.decompress(base64.b64decode(body)).decode("utf-8"))
    written = []
    for relative, content in sorted(files.items()):
        target = ROOT / relative
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        written.append(relative)
    return written


class SummaryResult(unittest.TextTestResult):
    """Track method outcomes, including failures inside subTests."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed_count = 0
        self.failed_methods = set()
        self.error_methods = set()

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed_count += 1

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed_methods.add(test.id())

    def addError(self, test, err):
        super().addError(test, err)
        self.error_methods.add(test.id())

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None:
            collection = (self.failed_methods if issubclass(err[0], test.failureException)
                          else self.error_methods)
            collection.add(test.id())


def main():
    if sys.version_info < (3, 9):
        print("Python 3.9 or newer is required.", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("part", nargs="?", default="all",
                        choices=[str(p) for p in range(1, LAST_PART + 1)] + ["all"],
                        help="run Parts 1 to PART (default: every open part)")
    args = parser.parse_args()
    top = highest_open_part()
    last_part = top if args.part == "all" else int(args.part)
    if last_part > top:
        print("Part %d is still sealed. Pass Parts 1 to %d first:  python3 test.py %d"
              % (last_part, top, top))
        return 2

    modules = ["tests.test_part%d" % part for part in range(1, last_part + 1)]
    suite = unittest.defaultTestLoader.loadTestsFromNames(modules)
    label = "Part 1" if last_part == 1 else "Parts 1–%d" % last_part
    print("Running %s (failures in the starter are expected)." % label, flush=True)
    print("Test files: " + ", ".join(module.replace(".", "/") + ".py"
                                      for module in modules), flush=True)
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout,
                                    resultclass=SummaryResult).run(suite)
    status = "PASS" if result.wasSuccessful() else "FAIL"
    print("\nSUMMARY: %s | %d tests run | %d passed | %d failed | %d errors | %d skipped" % (
        status, result.testsRun, result.passed_count,
        len(result.failed_methods - result.error_methods), len(result.error_methods),
        len(result.skipped)), flush=True)
    if result.expectedFailures or result.unexpectedSuccesses:
        print("Expected failures: %d | Unexpected successes: %d" % (
            len(result.expectedFailures), len(result.unexpectedSuccesses)))

    if result.wasSuccessful() and last_part == top and top < LAST_PART:
        nxt = top + 1
        written = unseal(nxt)
        if written:
            print("\nPart %d is now open. New files:" % nxt)
            for relative in written:
                print("  " + relative)
            print("Next: read rounds/part%d.md, then  python3 test.py %d" % (nxt, nxt))
    elif result.wasSuccessful() and top == LAST_PART and last_part == top:
        print("\nAll four parts pass. That is everything.")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
