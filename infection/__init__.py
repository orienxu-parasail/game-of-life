"""Contagion, a Game of Life variant. One module per part; implement the stub in each.

Parts open one at a time (see README). A function whose part is still sealed
raises AttributeError with a hint instead of ImportError.
"""

import importlib

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

_PART_OF = {
    "time_to_full_infection": 1,
    "time_to_full_infection_with_immunity": 2,
    "time_to_stable_state": 3,
    "time_to_full_infection_threshold": 4,
}

__all__ = ["DIRECTIONS"] + list(_PART_OF)


def __getattr__(name):
    part = _PART_OF.get(name)
    if part is None:
        raise AttributeError("module 'infection' has no attribute %r" % name)
    try:
        module = importlib.import_module(".part%d" % part, __name__)
    except ModuleNotFoundError as exc:
        if exc.name == "%s.part%d" % (__name__, part):
            raise AttributeError(
                "%s belongs to Part %d, which is still sealed. Pass the earlier "
                "parts with  python3 test.py  to open it." % (name, part)) from None
        raise
    return getattr(module, name)
