from input_loader import load_input_lines
from typing import List, Callable, Tuple

INPUT = load_input_lines(day=4)
Interval = Tuple[int, int]


def part1(lines: List[str]) -> int:
    return _count(lines, predicate=_is_contains)


def part2(lines: List[str]) -> int:
    return _count(lines, predicate=_is_overlap)


def _count(lines: List[str], predicate: Callable) -> int:
    count = 0

    for line in lines:
        a, b = _parse(line)
        if predicate(a, b) or predicate(b, a):
            count += 1

    return count


def _parse(line: str) -> Tuple[Interval, Interval]:
    first, second = line.split(",")
    return _to_interval(first), _to_interval(second)


def _to_interval(s: str) -> Interval:
    mini, maxi = s.split("-")
    return int(mini), int(maxi)


def _is_contains(a: Interval, b: Interval) -> bool:
    return a[0] >= b[0] and a[1] <= b[1]


def _is_overlap(a: Interval, b: Interval) -> bool:
    return a[0] <= b[0] <= a[1]


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
