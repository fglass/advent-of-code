from input_loader import load_input_lines
from typing import List, Tuple, Iterator

INPUT = load_input_lines(day=14)

AIR, ROCK, SAND = ".", "#", "o"
SAND_DIRECTIONS = [(0, 1), (-1, 1), (1, 1)]
SAND_START = (500, 0)
MAX_X = 750
FLOOR_OFFSET = 2

Cave = List[List[str]]
Coord = Tuple[int, int]


def part1(paths: List[str]) -> int:
    return _count_sand(paths)


def part2(paths: List[str]) -> int:
    return _count_sand(paths, with_floor=True)


def _count_sand(paths: List[str], with_floor: bool = False) -> int:  # Simulation
    cave = _init_cave(paths, with_floor)
    n_units = 0

    while _produce_sand(cave, with_floor):
        n_units += 1

    return n_units


def _init_cave(paths: List[str], with_floor: bool) -> Cave:
    cave = []
    rocks = set()
    max_y = 0

    for rock in _get_rocks(paths):
        rocks.add(rock)
        max_y = max(max_y, rock[1])

    if with_floor:
        max_y += FLOOR_OFFSET

    for y in range(max_y + 1):
        is_floor = y == max_y and with_floor
        cave.append([])

        for x in range(MAX_X):
            tile = ROCK if is_floor or (x, y) in rocks else AIR
            cave[-1].append(tile)

    return cave


def _get_rocks(paths: List[str]) -> Iterator[Coord]:
    for (sx, sy), (ex, ey) in _get_rock_lines(paths):
        if sx == ex:
            local_min_y = min(sy, ey)
            local_max_y = max(sy, ey)
            for y in range(local_min_y, local_max_y + 1):
                yield sx, y
        else:
            local_min_x = min(sx, ex)
            local_max_x = max(sx, ex)
            for x in range(local_min_x, local_max_x + 1):
                yield x, sy


def _get_rock_lines(paths: List[str]) -> Iterator[Tuple[Coord, Coord]]:
    for path in paths:
        points = path.split(" -> ")
        prev = None

        for point in points:
            x, y = point.split(",")
            curr = (int(x), int(y))

            if prev is not None:
                yield prev, curr

            prev = curr


def _produce_sand(cave: Cave, with_floor: bool) -> bool:
    sand_x, sand_y = SAND_START
    if cave[sand_y][sand_x] == SAND:
        return False

    pos = SAND_START
    at_rest = False

    while not at_rest:
        at_rest = True

        for dx, dy in SAND_DIRECTIONS:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if _is_unblocked(new_pos, cave):
                pos = new_pos
                at_rest = False
                break

        in_abyss = not with_floor and pos[1] >= len(cave) - 1
        if in_abyss:
            return False

    x, y = pos
    cave[y][x] = SAND
    return True


def _is_unblocked(pos: Coord, cave: Cave) -> bool:
    x, y = pos
    return 0 <= y < len(cave) and 0 <= x < len(cave[0]) and cave[y][x] not in {ROCK, SAND}


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
