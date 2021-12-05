from input_loader import load_input_lines

INPUT = load_input_lines(day=5)


def part1(lines: list) -> int:
    return _count_line_overlaps(lines, ignore_diagonal=True)


def part2(lines: list) -> int:
    return _count_line_overlaps(lines, ignore_diagonal=False)


def _count_line_overlaps(lines: list, ignore_diagonal: bool):
    overlaps = {}

    for line in lines:
        x1, y1, x2, y2 = _parse_line(line)

        if ignore_diagonal and _is_diagonal(x1, y1, x2, y2):
            continue

        for point in _get_points_on_line(x1, y1, x2, y2):
            overlaps[point] = overlaps.get(point, 0) + 1

    return len([n for n in overlaps.values() if n >= 2])


def _parse_line(line: str) -> list:
    return [int(n) for coord in line.split(" -> ") for n in coord.split(",")]


def _is_diagonal(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x1 != x2 and y1 != y2


def _get_points_on_line(x1: int, y1: int, x2: int, y2: int) -> list:
    dx = (x2 > x1) - (x2 < x1)
    dy = (y2 > y1) - (y2 < y1)
    length = max(abs(x2 - x1), abs(y2 - y1)) + 1
    return [(x1 + dx * n, y1 + dy * n) for n in range(length)]


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
