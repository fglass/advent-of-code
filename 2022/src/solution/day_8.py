import math
from enum import Enum
from input_loader import load_input_lines
from typing import List, Tuple, Iterator

INPUT = load_input_lines(day=8)
Grid = List[List[int]]


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def is_vertical(self) -> bool:
        return self == Direction.UP or self == Direction.DOWN


def part1(rows: List[str]) -> int:  # Inefficient: O(mn(m + n))
    grid = _create_grid(rows)
    n_cols, n_rows = len(grid), len(grid[0])
    n_visible = 0

    for y in range(n_cols):
        for x in range(n_rows):
            if _is_visible(grid, x, y):
                n_visible += 1

    return n_visible


def part2(rows: List[str]) -> int:
    grid = _create_grid(rows)
    n_cols, n_rows = len(grid), len(grid[0])
    max_scenic_score = 0

    for y in range(n_cols):
        for x in range(n_rows):
            scenic_score = _calculate_scenic_score(grid, x, y)
            max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score


def _create_grid(rows: List[str]) -> Grid:
    return [[int(tree) for tree in row] for row in rows]


def _is_visible(grid: Grid, x: int, y: int) -> bool:
    if _is_on_edge(grid, x, y):
        return True

    return any(
        _get_visibility_and_viewing_distance(grid, x, y, direction)[0] for direction in Direction
    )


def _calculate_scenic_score(grid: Grid, x: int, y: int) -> int:
    if _is_on_edge(grid, x, y):
        return 0

    return math.prod(
        _get_visibility_and_viewing_distance(grid, x, y, direction)[1] for direction in Direction
    )


def _is_on_edge(grid: Grid, x: int, y: int) -> bool:
    return x == 0 or y == 0 or y == len(grid) - 1 or x == len(grid[0]) - 1


def _get_visibility_and_viewing_distance(grid: Grid, x: int, y: int, direction: Direction) -> Tuple[bool, int]:  # O(m + n)
    tree = grid[y][x]
    is_visible = True
    viewing_distance = 0

    for i in _get_path_to_edge(grid, x, y, direction):
        viewing_distance += 1
        other_tree = grid[i][x] if direction.is_vertical() else grid[y][i]

        if other_tree >= tree:
            is_visible = False
            break

    return is_visible, viewing_distance


def _get_path_to_edge(grid: Grid, x: int, y: int, direction: Direction) -> Iterator[int]:
    if direction == Direction.UP:
        return range(y - 1, -1, -1)
    elif direction == Direction.DOWN:
        return range(y + 1, len(grid))
    elif direction == Direction.LEFT:
        return range(x - 1, -1, -1)
    else:
        return range(x + 1, len(grid[0]))


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
