# Part 4 — Threshold

Back to the three states of Part 2, with no recovery. The contagion rule now
takes a count, the way Life's rules do:

1. Any healthy cell with **at least N** infected neighbours becomes infected.
   Immune neighbours never count.
2. Any infected cell stays infected.
3. Any immune cell stays immune.

`N = 1` is exactly Part 2.

Return the number of generations until every healthy cell is infected. If a
generation changes nothing while healthy cells remain, the board has reached a
still life: return `-1`. If there is no healthy cell, return `0`.

## Code

Implement `time_to_full_infection_threshold` in `infection/part4.py`:

```python
def time_to_full_infection_threshold(grid: list[list[int]], N: int) -> int:
    """0 = healthy, 1 = infected, -1 = immune. N >= 1."""
```

## Examples

```text
1 0 1   N = 2    The middle cell has two infected neighbours   Output: 1

1 0 0 1 N = 2    Each healthy cell has only one. Still life.   Output: -1

1 1 1   N = 2    Generation 1: (1,1) has two                   Output: 3
1 0 0            Generation 2: (1,2) and (2,1)
1 0 0            Generation 3: (2,2)

1 1 1   N = 3    The bottom-right corner has only two          Output: -1
1 0 1            neighbours, so it can never reach three
1 1 0
```

## Your turn

1. Does the approach from Part 2 still work? Explain why or why not before
   changing anything.
2. Implement it, and give the time complexity in terms of `m`, `n`, and the
   number of generations.
3. Add one test for a case the supplied tests don't cover.

## Commands

```sh
python3 -m unittest tests.test_part4 -v     # this part's tests
python3 play.py 4 "1 0 1" 2                  # last argument is N
python3 test.py 4                           # Parts 1 to 4 together
```
