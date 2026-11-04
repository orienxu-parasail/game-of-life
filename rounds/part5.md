# Part 5 — Competing strains

Several strains spread on one board. An infected cell holds the id of its
strain, a positive integer. Healthy is still `0` and immune is still `-1`.
The rules:

1. Any healthy cell with at least one infected neighbour becomes infected by
   the strain that has **the most** infected neighbours around it. If two
   strains tie, the **smaller id** wins.
2. Any infected cell keeps its strain forever.
3. Any immune cell stays immune.

As always, every generation is computed from the board as it was at the end of
the previous one. The board has settled when a generation changes nothing.
Return the number of generations that changed something, together with the
final board.

## Code

Implement `simulate_competition` in `infection/part5.py`:

```python
def simulate_competition(grid: list[list[int]]) -> tuple[int, list[list[int]]]:
    """0 = healthy, -1 = immune, k >= 1 = infected by strain k."""
```

## Examples

```text
1 0 0 0 2        Generation 1: 1 1 0 2 2                    Output: (2, [[1, 1, 1, 2, 2]])
                 Generation 2: the middle cell sees one of
                               each; the smaller id wins

0 2 0            Generation 1: (1,1) sees 2, 1, 2 -> strain 2  Output: (2, [[1, 2, 2],
1 0 2                          (0,0) sees 1, 2 -> tie -> 1               [1, 2, 2],
0 0 0            Generation 2: (2,1) sees 2, 1, 2 -> strain 2            [1, 2, 2]])

1 -1 2           Still life from the start                  Output: (0, [[1, -1, 2]])
```

## Your turn

1. Implement it.
2. The Part 1 answer was a BFS. Can BFS still decide which strain takes a cell
   here? Where exactly does it break down?
3. Add one test for a case the supplied tests don't cover.

## Commands

```sh
python3 -m unittest tests.test_part5 -v     # this part's tests
python3 play.py 5 "1 0 0 0 2"
python3 test.py 5                           # Parts 1 to 5 together
```
