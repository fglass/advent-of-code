import functools
import sys
from input_loader import load_input_lines
from typing import Generator

INPUT = load_input_lines(day=9)
BASIN_BOUNDARY = 9
N_LARGEST_BASINS = 3


def part1(puzzle_input: list) -> int:
    height_map = _build_height_map(puzzle_input)
    lowest_points = _generate_lowest_points(height_map)
    return functools.reduce(lambda acc, point: acc + point[1] + 1, lowest_points, 0)


def part2(puzzle_input: list) -> int:
    height_map = _build_height_map(puzzle_input)
    basin_sizes = []

    for position, _ in _generate_lowest_points(height_map):
        basin_size = _calculate_basin_size(height_map, position) + 1
        basin_sizes.append(basin_size)

    largest_basins = sorted(basin_sizes, reverse=True)[:N_LARGEST_BASINS]
    return functools.reduce(lambda acc, value: acc * value, largest_basins)


def _build_height_map(puzzle_input: list) -> list:
    height_map = []

    for entry in puzzle_input:
        row = [int(n) for n in entry]
        height_map.append(row)

    return height_map


def _generate_lowest_points(height_map: list) -> Generator:
    for y, row in enumerate(height_map):
        for x, n in enumerate(row):
            position = (x, y)
            adjacent_positions = _get_adjacent_positions(height_map, position)

            if all(n < value for _, value in adjacent_positions):
                yield position, n


def _calculate_basin_size(height_map: list, position: tuple, visited: set = None) -> int:
    if visited is None:
        visited = set()

    basin_size = 0
    parent_value = _get_value(height_map, position)

    for adjacent, value in _get_adjacent_positions(height_map, position):
        if adjacent not in visited and parent_value <= value < BASIN_BOUNDARY:
            visited.add(adjacent)
            basin_size += _calculate_basin_size(height_map, adjacent, visited) + 1

    return basin_size


def _get_adjacent_positions(height_map: list, position: tuple) -> list:
    x, y = position
    adjacent_positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(pos, _get_value(height_map, pos)) for pos in adjacent_positions]


def _get_value(height_map: list, position: tuple) -> int:
    x, y = position

    if 0 <= y < len(height_map) and 0 <= x < len(height_map[0]):
        return height_map[y][x]

    return sys.maxsize


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
