import re
from input_loader import load_input_lines
from typing import List, Tuple

INPUT = load_input_lines(day=15)
LINE_PATTERN = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
Coord = Tuple[int, int]
Reading = Tuple[Coord, Coord]


def part1(report: List[str], row: int) -> int:
    readings = _parse_report(report)
    ranges = _get_covered_ranges(readings, row)

    n_covered = 0
    prev_end = float("-inf")

    for start, end in ranges:
        diff = end - max(start, prev_end)

        if diff > 0:
            n_covered += diff

        prev_end = max(end, prev_end)

    return n_covered


def part2(report: List[str], upper_bound: int) -> int:
    readings = _parse_report(report)

    for y in range(upper_bound):
        prev_end = float("-inf")

        for start, end in _get_covered_ranges(readings, y):
            if start > upper_bound:
                break

            if prev_end >= 0 and start - prev_end > 1:
                distress_beacon = (start - 1, y)
                return _calculate_tuning_frequency(distress_beacon)

            prev_end = max(end, prev_end)

    return -1


def _parse_report(report: List[str]) -> List[Reading]:
    readings = []

    for line in report:
        matches = [int(x) for x in re.match(LINE_PATTERN, line).groups()]
        readings.append(((matches[0], matches[1]), (matches[2], matches[3])))

    return readings


def _get_covered_ranges(readings: List[Reading], row: int) -> List[Tuple[int, int]]:
    ranges = []

    for sensor, beacon in readings:
        distance_to_row = abs(sensor[1] - row)
        distance_to_beacon = _manhattan_distance(sensor, beacon)
        distance = distance_to_beacon - distance_to_row

        if distance > 0:
            ranges.append((sensor[0] - distance, sensor[0] + distance))

    return sorted(ranges)


def _manhattan_distance(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _calculate_tuning_frequency(beacon: Coord) -> int:
    return beacon[0] * 4000000 + beacon[1]


if __name__ == "__main__":
    print(f"part1={part1(INPUT, row=2_000_000)}")
    print(f"part2={part2(INPUT, upper_bound=4_000_000)}")  # Brute-force = 30s
