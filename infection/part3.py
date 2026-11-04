"""Part 3: recovery. See rounds/part3.md."""

from typing import List


def time_to_stable_state(grid: List[List[int]], D: int) -> int:
    """Return the first day on which no cell is infected.

    grid: m x n board (m rows, n columns), 0 = healthy, 1 = infected on day 0, -1 = immune. D >= 1.
    Each day, in order: (1) every healthy cell with an infected neighbour
    becomes infected; (2) every cell that has now been infected for D days
    becomes immune (-1). Return 0 if no cell is infected at the start.
    """
    raise NotImplementedError("Part 3: implement time_to_stable_state")
