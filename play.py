"""Run one part's function on a board typed on the command line.

    python3 play.py 1 "0 0 0 / 0 1 0 / 0 0 0"
    python3 play.py 2 "1 -1 0 / 0 -1 0 / 0 0 0"
    python3 play.py 3 "1 0 0" 1          # third argument is D
    python3 play.py 4 "1 0 1" 2          # third argument is N
    python3 play.py 5 "1 0 0 0 2"

Rows are separated by "/" and cells by spaces.
"""

import sys

import infection


def parse(text):
    return [[int(cell) for cell in row.split()] for row in text.split("/") if row.strip()]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    part = argv[0]
    grid = parse(argv[1])
    extra = [int(x) for x in argv[2:]]
    func = {
        "1": infection.time_to_full_infection,
        "2": infection.time_to_full_infection_with_immunity,
        "3": infection.time_to_stable_state,
        "4": infection.time_to_full_infection_threshold,
        "5": infection.simulate_competition,
    }.get(part)
    if func is None:
        print("part must be 1-5", file=sys.stderr)
        return 2
    for row in grid:
        print(" ".join("%2d" % cell for cell in row))
    result = func(grid, *extra)
    if part == "5":
        steps, final = result
        print("steps:", steps)
        for row in final:
            print(" ".join("%2d" % cell for cell in row))
    else:
        print("result:", result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
