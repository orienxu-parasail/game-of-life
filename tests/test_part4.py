"""Part 4 tests (11). Run from the exercise folder: python3 test.py 4"""

from infection import time_to_full_infection_threshold
from tests.support import GridTestCase


class Part4Tests(GridTestCase):
    def check(self, text, N, expected):
        self.assert_result(time_to_full_infection_threshold, text, expected, N)

    def test_N1_behaves_like_part1(self):
        self.check("""
            0 0 0
            0 1 0
            0 0 0
        """, 1, 2)

    def test_cell_between_two_sources(self):
        self.check("1 0 1", 2, 1)

    def test_gap_too_wide(self):
        self.check("1 0 0 1", 2, -1)

    def test_diagonal_sources(self):
        self.check("""
            1 0
            0 1
        """, 2, 1)

    def test_single_row_of_sources_stalls(self):
        self.check("""
            1 1 1
            0 0 0
            0 0 0
        """, 2, -1)

    def test_L_shape_spreads_diagonally(self):
        self.check("""
            1 1 1
            1 0 0
            1 0 0
        """, 2, 3)

    def test_frame(self):
        self.check("""
            1 1 1 1
            1 0 0 1
            1 0 0 1
            1 1 1 1
        """, 2, 1)

    def test_corner_can_never_reach_three(self):
        self.check("""
            1 1 1
            1 0 1
            1 1 0
        """, 3, -1)

    def test_interior_cell_with_four_sources(self):
        self.check("""
            1 1 1
            1 0 1
            1 1 1
        """, 4, 1)

    def test_immune_neighbour_does_not_count(self):
        self.check("""
            1 1  1
            1 0 -1
            1 0  0
        """, 2, -1)

    def test_already_full(self):
        self.check("""
            1 -1
            1  1
        """, 3, 0)
