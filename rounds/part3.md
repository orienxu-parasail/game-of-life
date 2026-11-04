# Part 3 — Recovery

Infected cells now recover. A cell that has been infected for **D generations**
becomes immune, and immune cells never change again. The generation is called a
day. The rules, applied in this order on each day:

1. Any healthy cell with at least one infected neighbour becomes infected.
2. Any cell that has now been infected for `D` days becomes immune. Cells that
   start infected count as infected on day 0, so they turn immune at the end of
   day `D`.

A cell infected on day `t` therefore spreads on days `t+1 … t+D` and is immune
from the end of day `t+D`.

Eventually the board settles: every cell is healthy or immune and nothing can
change again. Return the first day on which no cell is infected. If no cell is
infected at the start, return `0`.

## Code

Implement `time_to_stable_state` in `infection/part3.py`:

```python
def time_to_stable_state(grid: list[list[int]], D: int) -> int:
    """0 = healthy, 1 = infected on day 0, -1 = immune. D >= 1."""
```

## Examples

```text
1 0 0   D = 1    Day 1: cell 1 infected, cell 0 immune       Output: 3
                 Day 2: cell 2 infected, cell 1 immune
                 Day 3: cell 2 immune. The board is settled.

0 0 0   D = 2    Day 1: edges infected                        Output: 4
0 1 0            Day 2: corners infected, centre immune
0 0 0            Day 3: edges immune
                 Day 4: corners immune

 1 -1 0  D = 2   The source recovers on day 2. The healthy    Output: 2
-1 -1 0          cells are never reached, and that is fine:
 0  0 0          the question is when the board settles.
```

## Your turn

1. What state does each cell need now? Sketch it before coding.
2. Implement it. Then tell me: is there a way to get the answer without
   simulating day by day? When would that shortcut stop being valid?
3. Add one test for a case the supplied tests don't cover.

## Commands

```sh
python3 -m unittest tests.test_part3 -v     # this part's tests
python3 play.py 3 "1 0 0" 1                  # last argument is D
python3 test.py 3                           # Parts 1 to 3 together
```
