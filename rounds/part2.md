# Part 2 — Immune cells

A third state joins the board: **immune (-1)**. Think of a vaccinated cell, or
a wall. The rules become:

1. Any healthy cell with at least one infected neighbour becomes infected.
2. Any infected cell stays infected.
3. Any immune cell stays immune. It is never infected and never counts as an
   infected neighbour.

Return the number of generations until every **healthy** cell is infected.
If some healthy cell can never be reached, return `-1`. If the board has no
healthy cell to begin with, return `0`.

## Code

Implement `time_to_full_infection_with_immunity` in `infection/part2.py`:

```python
def time_to_full_infection_with_immunity(grid: list[list[int]]) -> int:
    """0 = healthy, 1 = infected, -1 = immune."""
```

## Examples

```text
 1 -1  0     The front goes around the wall:             Output: 6
 0 -1  0     down, down, right, right, up, up
 0  0  0

 1 -1  0     The healthy cells are sealed off            Output: -1
-1 -1  0
 0  0  0

 1 -1        No healthy cell                             Output: 0
-1  1
```

## Your turn

1. Say what changes compared with Part 1, then make the change.
2. Add one test for a case the supplied tests don't cover.

## Commands

```sh
python3 -m unittest tests.test_part2 -v     # this part's tests
python3 play.py 2 "1 -1 0 / 0 -1 0 / 0 0 0"
python3 test.py 2                           # Parts 1 to 2 together
```
