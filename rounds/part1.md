# Part 1 — Contagion

A board is an `m × n` grid of cells, `m` rows by `n` columns. Each cell has a state: **healthy (0)** or
**infected (1)**. Every cell interacts with its four orthogonal neighbours
(up, down, left, right; diagonals are not neighbours here) by one rule:

1. Any healthy cell with **at least one** infected neighbour becomes infected,
   as if by contagion.
2. Any infected cell stays infected.

The next generation of the board is determined by applying the rule
simultaneously to every cell of the current generation. All infections in a
generation happen at once, based on the board as it was.

Return the number of generations until **every** cell is infected, or `-1` if
the board never gets there.

## Code

Implement `time_to_full_infection` in `infection/part1.py`:

```python
def time_to_full_infection(grid: list[list[int]]) -> int:
    """0 = healthy, 1 = infected. Generations until all cells are 1, or -1."""
```

The board has at least one row and one column. You may update it in place.

## Examples

```text
0 0 0        Generation 1: the 4 neighbours of the centre   Output: 2
0 1 0        Generation 2: the corners
0 0 0

1 0 0        Generation 1: neighbours of both corners       Output: 2
0 0 0        Generation 2: the two fronts meet
0 0 1

0 0 0        No infected cell. The board is still life.     Output: -1
0 0 0

1 1          Already full                                   Output: 0
1 1
```

## Your turn

1. Describe your approach and its time and space complexity before coding.
2. Implement it and make the tests pass.
3. Add one test for a case the supplied tests don't cover.

## Commands

```sh
python3 -m unittest tests.test_part1 -v     # this part's tests
python3 play.py 1 "0 0 0 / 0 1 0 / 0 0 0"
python3 test.py 1                           # when this passes, Part 2 opens
```
