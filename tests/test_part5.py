"""Part 5 tests (9). Run from the exercise folder: python3 test.py 5"""

from infection import simulate_competition
from tests.support import GridTestCase, grid


class Part5Tests(GridTestCase):
    def check(self, text, steps, final):
        self.assert_result(simulate_competition, text, (steps, grid(final)))

    def test_single_virus_behaves_like_part1(self):
        self.check("""
            0 0 0
            0 1 0
            0 0 0
        """, 2, """
            1 1 1
            1 1 1
            1 1 1
        """)

    def test_tie_goes_to_smaller_id(self):
        self.check("1 0 0 0 2", 2, "1 1 1 2 2")

    def test_tie_goes_to_smaller_id_regardless_of_position(self):
        self.check("2 0 0 0 1", 2, "2 2 1 1 1")

    def test_even_line_has_no_tie(self):
        self.check("1 0 0 0 0 2", 2, "1 1 1 2 2 2")

    def test_majority_wins(self):
        self.check("""
            0 2 0
            1 0 2
            0 0 0
        """, 2, """
            1 2 2
            1 2 2
            1 2 2
        """)

    def test_walls_separate_viruses(self):
        self.check("""
            1 -1 2
            0 -1 0
            0  0 0
        """, 3, """
            1 -1 2
            1 -1 2
            1  1 2
        """)

    def test_already_stable(self):
        self.check("1 -1 2", 0, "1 -1 2")

    def test_no_virus(self):
        self.check("""
            0  0
            0 -1
        """, 0, """
            0  0
            0 -1
        """)

    def test_larger_grid(self):
        self.check("""
            1 0  0 0 0
            0 0  0 0 0
            0 0 -1 0 0
            0 0  0 0 0
            0 0  0 0 3
        """, 4, """
            1 1  1 1 1
            1 1  1 1 3
            1 1 -1 3 3
            1 1  3 3 3
            1 3  3 3 3
        """)
