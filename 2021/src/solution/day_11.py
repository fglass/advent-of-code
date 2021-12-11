import functools
from input_loader import load_input_lines

INPUT = load_input_lines(day=11)
STEPS = 100
GRID_SIZE = 10
FLASH_THRESHOLD = 9


def part1(puzzle_input: list) -> int:
    grid = _build_grid(puzzle_input)
    return functools.reduce(lambda acc, _: acc + _tick(grid), range(STEPS), 0)


def part2(puzzle_input: list) -> int:
    grid = _build_grid(puzzle_input)
    step = 1

    while _tick(grid) != GRID_SIZE * GRID_SIZE:
        step += 1

    return step


def _build_grid(puzzle_input: list) -> list:
    grid = []

    for entry in puzzle_input:
        row = [int(n) for n in entry]
        grid.append(row)

    return grid


def _tick(grid: list) -> int:
    flashed = _process_octopuses(grid)
    [_reset_energy(grid, x, y) for x, y in flashed]
    return len(flashed)


def _process_octopuses(grid: list) -> set:
    flashed = set()

    for y, row in enumerate(grid):
        for x, number in enumerate(row):
            energy = _get_and_increment_energy(grid, x, y)

            if energy > FLASH_THRESHOLD and (x, y) not in flashed:
                _flash(grid, x, y, flashed)

    return flashed


def _flash(grid: list, x: int, y: int, flashed: set):
    flashed.add((x, y))

    adjacent_positions = [
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
        (x - 1, y),     (x, y),     (x + 1, y),
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
    ]

    for position in adjacent_positions:
        adj_x, adj_y = position

        if not _is_valid_position(grid, adj_x, adj_y) or position in flashed:
            continue

        energy = _get_and_increment_energy(grid, adj_x, adj_y)

        if energy > FLASH_THRESHOLD:
            _flash(grid, adj_x, adj_y, flashed)


def _get_energy(grid: list, x: int, y: int) -> int:
    return grid[y][x]


def _get_and_increment_energy(grid: list, x: int, y: int) -> int:
    grid[y][x] += 1
    return grid[y][x]


def _reset_energy(grid: list, x: int, y: int):
    grid[y][x] = 0


def _is_valid_position(grid: list, x: int, y: int) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
