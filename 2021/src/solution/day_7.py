import functools
from input_loader import load_input_line
from math import floor, ceil
from typing import Callable

INPUT = load_input_line(day=7)


def part1(puzzle_input: str) -> int:
    positions = sorted(_get_positions(puzzle_input))
    median_idx = round(len(positions) / 2)
    median_pos = positions[median_idx]

    return _calculate_fuel_used(positions, dest=median_pos, cost_fn=lambda n: n)


def part2(puzzle_input: str) -> int:
    positions = _get_positions(puzzle_input)
    mean_pos = sum(positions) / len(positions)

    optimum_positions = [floor(mean_pos), ceil(mean_pos)]
    fuels_used = [
        _calculate_fuel_used(positions, dest=pos, cost_fn=lambda n: n * (n + 1) / 2) for pos in optimum_positions
    ]

    return min(fuels_used)


def _get_positions(puzzle_input: str) -> list:
    return [int(pos) for pos in puzzle_input.split(",")]


def _calculate_fuel_used(positions: list, dest: int, cost_fn: Callable) -> int:
    fuel_used = functools.reduce(lambda acc, pos: acc + cost_fn(_calculate_distance(pos, dest)), positions, 0)
    return int(fuel_used)


def _calculate_distance(src: int, dest: int) -> int:
    return abs(src - dest)


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
