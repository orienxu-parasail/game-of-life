"""Part 1: basic infection. See rounds/part1.md."""

from typing import List


def time_to_full_infection(grid: List[List[int]]) -> int:
    """Return the number of generations until every cell is infected, or -1.

    grid: m x n board (m rows, n columns), 0 = healthy, 1 = infected. At least one row and column.
    Rule: any healthy cell with at least one infected neighbour (up, down,
    left, right) becomes infected. Each generation is computed from the board
    as it was at the end of the previous one. You may update it in place.
    """
    raise NotImplementedError("Part 1: implement time_to_full_infection")
