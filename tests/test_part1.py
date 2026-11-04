"""Part 1 tests (10). Run from the exercise folder: python3 -m unittest tests.test_part1 -v"""

from infection import time_to_full_infection
from tests.support import GridTestCase


class Part1Tests(GridTestCase):
    def check(self, text, expected):
        self.assert_result(time_to_full_infection, text, expected)

    def test_center(self):
        self.check("""
            0 0 0
            0 1 0
            0 0 0
        """, 2)

    def test_two_corners(self):
        self.check("""
            1 0 0
            0 0 0
            0 0 1
        """, 2)

    def test_no_source(self):
        self.check("""
            0 0
            0 0
        """, -1)

    def test_already_full(self):
        self.check("""
            1 1
            1 1
        """, 0)

    def test_single_cell(self):
        self.check("1", 0)
        self.check("0", -1)

    def test_line(self):
        self.check("1 0 0 0 0", 4)

    def test_column(self):
        self.check("""
            0
            0
            1
            0
            0
            0
        """, 3)

    def test_larger_grid(self):
        self.check("""
            0 0 0 0 0
            0 0 0 0 0
            0 0 1 0 0
            0 0 0 0 0
            0 0 0 0 0
        """, 4)

    def test_rectangle(self):
        self.check("""
            1 0 0 0
            0 0 0 0
        """, 4)

    def test_ring_around_one_healthy_cell(self):
        self.check("""
            1 1 1
            1 0 1
            1 1 1
        """, 1)
