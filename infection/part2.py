"""Part 2: immune cells. See rounds/part2.md."""

from typing import List


def time_to_full_infection_with_immunity(grid: List[List[int]]) -> int:
    """Return the number of generations until every healthy cell is infected, or -1.

    grid: m x n board (m rows, n columns), 0 = healthy, 1 = infected, -1 = immune.
    Immune cells never change and never count as infected neighbours. They do
    not count toward "everyone infected". Return 0 if there is no healthy cell.
    """
    raise NotImplementedError("Part 2: implement time_to_full_infection_with_immunity")
