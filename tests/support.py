"""Helpers shared by the test files."""

import copy
import unittest


def grid(text):
    """Parse a grid written as one row per line, cells separated by spaces.

    grid('''
        0 1 0
        0 0 -1
    ''') == [[0, 1, 0], [0, 0, -1]]
    """
    rows = [line.split() for line in text.strip().splitlines()]
    return [[int(cell) for cell in row] for row in rows if row]


class GridTestCase(unittest.TestCase):
    def assert_result(self, func, text, expected, *args):
        """func(grid, *args) == expected. The function receives a fresh copy."""
        g = grid(text)
        actual = func(copy.deepcopy(g), *args)
        self.assertEqual(actual, expected,
                         "\n%s(grid, %s) on\n%s\nexpected %r, got %r"
                         % (func.__name__, ", ".join(map(repr, args)), text.strip("\n"),
                            expected, actual))
