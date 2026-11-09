# Contagion: a Game of Life variant

A board is an `m × n` grid of cells, `m` rows by `n` columns. Each cell has a
state, and each generation every cell interacts with its neighbours by a small
set of rules, applied simultaneously across the whole board. If you know
Conway's Game of Life, this is a cousin: the neighbourhood is the four
orthogonal cells instead of eight, and the rules describe an infection rather
than births and deaths.

There are five parts, and each one adds a rule. Only Part 1 is open when you
start. The rest are sealed in `locked/` and open one at a time: when every
test up to the current part passes, the next part's prompt, stub and tests are
written into the folder for you.

## Setup

Python 3.9 or newer, standard library only. From this folder:

```sh
./setup.sh            # Windows: py -3 setup.py
```

If setup fails, it prints what to fix. On Windows, use `py -3` instead of `python3`.

## How to work through it

Each part has a prompt in `rounds/`, a stub function in `infection/`, and a
test file in `tests/`. Every test fails until you implement the function.

1. Read `rounds/part1.md`.
2. Implement the function in `infection/part1.py`.
3. Run the tests until they pass:

   ```sh
   python3 -m unittest tests.test_part1 -v    # just this part, verbose
   python3 test.py                            # every open part; opens the next one on success
   ```

4. When `test.py` passes it prints the new files for the next part. Read the
   new prompt and repeat.

Other useful commands:

```sh
python3 test.py 2                                    # Parts 1 and 2 together (once Part 2 is open)
python3 -m unittest tests.test_part1 -k corners -v   # only tests whose names match
python3 play.py 1 "0 0 0 / 0 1 0 / 0 0 0"            # run your Part 1 code on a board
```

## Cell states

| Value | State |
| --- | --- |
| `0` | healthy |
| `1` | infected |

Later parts introduce more states; each prompt defines the ones it uses.
Neighbours are the four cells up, down, left, and right. Diagonals never count.
Every generation is computed from the board as it was at the end of the
previous one: all changes in a generation happen at once. Your functions may
update the board they are given in place; the tests always pass a fresh copy.

## Ground rules

- Think aloud. State your approach and its complexity before you code.
- Work on the open part only, and keep your changes as you move on. Later
  parts may reuse earlier ones.
- Don't weaken the supplied tests; the interviewer may run more tests against
  your code. Decoding `locked/` by hand defeats the point of the exercise.
- Use any editor, debugger, or print statements. Plan for about 45 minutes;
  it's fine not to finish every part.
