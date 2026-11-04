# Contagion: a Game of Life variant

A board is an `m × n` grid of cells, `m` rows by `n` columns. Each cell has a state, and each generation
every cell interacts with its neighbours by a small set of rules, applied
simultaneously across the whole board. If you know Conway's Game of Life, this
is a cousin: the neighbourhood is the four orthogonal cells instead of eight,
and the rules describe an infection rather than births and deaths.

There are five parts, and each one adds a rule. Each part has a prompt in
`rounds/`, a stub function in `infection/`, and a test file in `tests/` that
you can run straight away. Every test fails until you implement the function.

## Setup

Python 3.9 or newer, standard library only. From this folder:

```sh
./setup.sh            # Windows: py -3 setup.py
```

If setup fails, it prints what to fix. On Windows, use `py -3` instead of `python3`.

## How to work through it

Do the parts in order. For each one: read the prompt, implement the function in
the file it names, run that part's tests until they pass, then move on.

| Part | Read | Implement in | Run |
| --- | --- | --- | --- |
| 1 | [rounds/part1.md](rounds/part1.md) | `infection/part1.py` | `python3 -m unittest tests.test_part1 -v` |
| 2 | [rounds/part2.md](rounds/part2.md) | `infection/part2.py` | `python3 -m unittest tests.test_part2 -v` |
| 3 | [rounds/part3.md](rounds/part3.md) | `infection/part3.py` | `python3 -m unittest tests.test_part3 -v` |
| 4 | [rounds/part4.md](rounds/part4.md) | `infection/part4.py` | `python3 -m unittest tests.test_part4 -v` |
| 5 | [rounds/part5.md](rounds/part5.md) | `infection/part5.py` | `python3 -m unittest tests.test_part5 -v` |

Other useful commands:

```sh
python3 test.py 2                                    # Parts 1 and 2 together
python3 test.py all                                  # every part
python3 -m unittest tests.test_part1 -k corners -v   # only tests whose names match
python3 play.py 1 "0 0 0 / 0 1 0 / 0 0 0"            # run your Part 1 code on a board
python3 play.py 3 "1 0 0" 1                          # Part 3 with D = 1
python3 play.py 4 "1 0 1" 2                          # Part 4 with N = 2
```

## Cell states

| Value | State | From part |
| --- | --- | --- |
| `0` | healthy | 1 |
| `1` | infected (in Part 5: infected by strain 1) | 1 |
| `-1` | immune: never infected, never counts as a neighbour | 2 |
| `k ≥ 2` | infected by strain `k` | 5 |

Neighbours are the four cells up, down, left, and right. Diagonals never count.
Every generation is computed from the board as it was at the end of the
previous one: all changes in a generation happen at once. Your functions may
update the board they are given in place; the tests always pass a fresh copy.

## Ground rules

- Think aloud. State your approach and its complexity before you code.
- Read only the current part, and keep your changes as you move on. Later
  parts may reuse earlier ones.
- Don't weaken the supplied tests; the interviewer may run more tests against
  your code.
- Use any editor, debugger, or print statements. Plan for about 45 minutes;
  it's fine not to finish every part.
