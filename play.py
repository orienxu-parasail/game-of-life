"""Run one part's function on a board typed on the command line.

    python3 play.py 1 "0 0 0 / 0 1 0 / 0 0 0"
    python3 play.py PART "row / row / row" [EXTRA ...]

Rows are separated by "/" and cells by spaces. Parts that take an extra
argument say so in their prompt, with an example command.
"""

import sys

import infection

FUNCTIONS = {
    "1": "time_to_full_infection",
    "2": "time_to_full_infection_with_immunity",
    "3": "time_to_stable_state",
    "4": "time_to_full_infection_threshold",
    "5": "time_to_full_infection_threshold_fast",
}


def parse(text):
    return [[int(cell) for cell in row.split()] for row in text.split("/") if row.strip()]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    part = argv[0]
    if part not in FUNCTIONS:
        print("part must be 1-5", file=sys.stderr)
        return 2
    try:
        func = getattr(infection, FUNCTIONS[part])
    except AttributeError as exc:
        print(exc, file=sys.stderr)
        return 2
    grid = parse(argv[1])
    extra = [int(x) for x in argv[2:]]
    for row in grid:
        print(" ".join("%2d" % cell for cell in row))
    result = func(grid, *extra)
    if isinstance(result, tuple):
        steps, final = result
        print("steps:", steps)
        for row in final:
            print(" ".join("%2d" % cell for cell in row))
    else:
        print("result:", result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
