"""Part 2 tests (9). Run from the exercise folder: python3 test.py 2"""

from infection import time_to_full_infection_with_immunity
from tests.support import GridTestCase


class Part2Tests(GridTestCase):
    def check(self, text, expected):
        self.assert_result(time_to_full_infection_with_immunity, text, expected)

    def test_no_immune_cells_behaves_like_part1(self):
        self.check("""
            0 0 0
            0 1 0
            0 0 0
        """, 2)

    def test_sealed_off_cells_are_unreachable(self):
        self.check("""
            1 -1 0
           -1 -1 0
            0  0 0
        """, -1)

    def test_infection_goes_around_a_wall(self):
        self.check("""
            1 -1 0
            0 -1 0
            0  0 0
        """, 6)

    def test_all_immune(self):
        self.check("""
            -1 -1
            -1 -1
        """, 0)

    def test_immune_and_infected_only(self):
        self.check("""
             1 -1
            -1  1
        """, 0)

    def test_no_source(self):
        self.check("""
             0 -1
            -1  0
        """, -1)

    def test_immune_cells_do_not_spread(self):
        self.check("1 -1 0", -1)

    def test_detour(self):
        self.check("""
             1  0  0 0
            -1 -1 -1 0
             0  0  0 0
        """, 8)

    def test_corridor(self):
        self.check("""
            1 -1 0  0 0
            0 -1 0 -1 0
            0 -1 0 -1 0
            0  0 0 -1 0
        """, 13)
