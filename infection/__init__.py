"""Contagion, a Game of Life variant. One module per part; implement the stub in each."""

from .part1 import time_to_full_infection
from .part2 import time_to_full_infection_with_immunity
from .part3 import time_to_stable_state
from .part4 import time_to_full_infection_threshold
from .part5 import simulate_competition

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

__all__ = [
    "DIRECTIONS",
    "time_to_full_infection",
    "time_to_full_infection_with_immunity",
    "time_to_stable_state",
    "time_to_full_infection_threshold",
    "simulate_competition",
]
