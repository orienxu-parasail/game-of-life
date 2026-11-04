#!/usr/bin/env python3
"""Run all tests up to the requested part; cases live in tests/test_partN.py."""

import argparse
import sys
import unittest


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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("part", nargs="?", default="1", choices=["1", "2", "3", "4", "5", "all"])
    args = parser.parse_args()
    last_part = 5 if args.part == "all" else int(args.part)
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
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
