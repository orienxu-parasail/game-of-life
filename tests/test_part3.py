"""Part 3 tests (9). Run from the exercise folder: python3 test.py 3"""

from infection import time_to_stable_state
from tests.support import GridTestCase


class Part3Tests(GridTestCase):
    def check(self, text, D, expected):
        self.assert_result(time_to_stable_state, text, expected, D)

    def test_line_recovers_one_day_after_spreading(self):
        self.check("1 0 0", 1, 3)

    def test_center_D1(self):
        self.check("""
            0 0 0
            0 1 0
            0 0 0
        """, 1, 3)

    def test_center_D2(self):
        self.check("""
            0 0 0
            0 1 0
            0 0 0
        """, 2, 4)

    def test_single_cell_waits_D_days(self):
        self.check("1", 3, 3)

    def test_no_infection_is_already_stable(self):
        self.check("""
            0 0
            0 0
        """, 2, 0)

    def test_all_immune_is_already_stable(self):
        self.check("-1 -1", 1, 0)

    def test_wall_D1(self):
        self.check("""
            1 -1 0
            0 -1 0
            0  0 0
        """, 1, 7)

    def test_sealed_source_stops_after_recovery(self):
        self.check("""
            1 -1 0
           -1 -1 0
            0  0 0
        """, 2, 2)

    def test_two_sources_meet(self):
        self.check("1 0 0 0 1", 1, 3)
