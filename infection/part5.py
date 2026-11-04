"""Part 5: competing viruses. See rounds/part5.md."""

from typing import List, Tuple


def simulate_competition(grid: List[List[int]]) -> Tuple[int, List[List[int]]]:
    """Run the board until it settles. Return (generations, final_board).

    grid: m x n board (m rows, n columns), 0 = healthy, -1 = immune, k >= 1 = infected by strain k.
    Rule: any healthy cell with at least one infected neighbour is taken by
    the strain with the most infected neighbours around it; ties go to the
    smallest id. Each generation is computed from the board as it was at the
    end of the previous one. Stop when a generation changes nothing, and count
    only the generations that changed something.
    """
    raise NotImplementedError("Part 5: implement simulate_competition")
