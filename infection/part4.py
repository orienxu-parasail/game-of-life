"""Part 4: infection threshold. See rounds/part4.md."""

from typing import List


def time_to_full_infection_threshold(grid: List[List[int]], N: int) -> int:
    """Return the number of generations until every healthy cell is infected, or -1.

    grid: m x n board (m rows, n columns), 0 = healthy, 1 = infected, -1 = immune. N >= 1.
    Rule: any healthy cell with at least N infected neighbours becomes
    infected. Immune neighbours never count. Return 0 if there is no healthy
    cell, and -1 if a generation changes nothing while healthy cells remain.
    """
    raise NotImplementedError("Part 4: implement time_to_full_infection_threshold")
