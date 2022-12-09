from input_loader import load_input_lines
from typing import List, Tuple

INPUT = load_input_lines(day=9)

Coord = Tuple[int, int]
DISTANCE_THRESHOLD = 2
DIRECTION_DELTAS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def part1(motions: List[str]) -> int:
    return _perform_motions(motions, knots=2)


def part2(motions: List[str]) -> int:
    return _perform_motions(motions, knots=10)


def _perform_motions(motions: List[str], knots: int) -> int:
    rope = [(0, 0) for _ in range(knots)]
    tail_positions = {rope[-1]}

    for motion in motions:
        direction, magnitude_str = motion.split()
        magnitude = int(magnitude_str)

        for _ in range(magnitude):
            rope[0] = _move_head(rope[0], direction)

            for i in range(1, knots):
                rope[i] = _move_knot(rope[i], rope[i - 1])

            tail_positions.add(rope[-1])

    return len(tail_positions)


def _move_head(head: Coord, direction: str) -> Coord:
    dx, dy = DIRECTION_DELTAS[direction]
    return _move_coord(head, dx, dy)


def _move_knot(curr: Coord, prev: Coord) -> Coord:
    dx = prev[0] - curr[0]
    dy = prev[1] - curr[1]

    if abs(dx) + abs(dy) > DISTANCE_THRESHOLD:
        return _move_coord(curr, dx, dy)
    if abs(dx) == DISTANCE_THRESHOLD:
        return _move_coord(curr, dx=dx, dy=0)
    if abs(dy) == DISTANCE_THRESHOLD:
        return _move_coord(curr, dx=0, dy=dy)

    return curr


def _move_coord(coord: Coord, dx: int, dy: int) -> Coord:
    return coord[0] + _normalize(dx), coord[1] + _normalize(dy)


def _normalize(delta: int) -> int:
    return delta // abs(delta) if delta != 0 else 0


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
