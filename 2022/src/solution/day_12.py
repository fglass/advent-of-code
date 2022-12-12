from input_loader import load_input_lines
from typing import List, Tuple

INPUT = load_input_lines(day=12)
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
MAX_CLIMB_HEIGHT = 1

Coord = Tuple[int, int]
HeightMap = List[List[int]]


def part1(grid: List[str]) -> int:
    height_map, starts, end = _parse_input_grid(grid)
    return _min_steps_to_end(height_map, starts, end)


def part2(grid: List[str]) -> int:
    height_map, starts, end = _parse_input_grid(grid, multi_start=True)
    return _min_steps_to_end(height_map, starts, end)


def _parse_input_grid(grid: List[str], multi_start: bool = False) -> Tuple[HeightMap, List[Coord], Coord]:
    height_map = []
    starts = []
    end = None

    for y, row in enumerate(grid):
        height_map.append([])

        for x, char in enumerate(row):
            if char == "S" or char == "a" and multi_start:
                starts.append((y, x))
                height = 0
            elif char == "E":
                end = (y, x)
                height = 26
            else:
                height = ord(char) - ord("a")

            height_map[-1].append(height)

    return height_map, starts, end


def _min_steps_to_end(height_map: HeightMap, starts: List[Coord], end: Coord) -> int:  # BFS
    m = len(height_map)
    n = len(height_map[0])

    next_level = [(y, x, 0) for y, x, in starts]
    steps = -1

    while len(next_level) > 0:
        current_level = next_level
        next_level = []
        steps += 1

        for curr_y, curr_x, height in current_level:
            if (curr_y, curr_x) == end:
                return steps

            for dy, dx in DIRS:
                next_y = curr_y + dy
                next_x = curr_x + dx

                if next_y < 0 or next_y >= m or next_x < 0 or next_x >= n:
                    continue

                next_height = height_map[next_y][next_x]

                if next_height - height > MAX_CLIMB_HEIGHT:
                    continue

                height_map[next_y][next_x] = float("inf")  # Mark as visited
                next_level.append((next_y, next_x, next_height))

    return -1


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
