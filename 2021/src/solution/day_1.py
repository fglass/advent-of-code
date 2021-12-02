from typing import Callable
from input_loader import load_input_sequence

INPUT = load_input_sequence(day=1)
WINDOW_SIZE = 3


def part1(measurements: list) -> int:
    return _calculate_number_of_increases(
        measurements,
        selection_strategy=lambda idx: measurements[idx]
    )


def part2(measurements: list) -> int:
    return _calculate_number_of_increases(
        measurements,
        selection_strategy=lambda idx: sum(measurements[idx: idx + WINDOW_SIZE])
    )


def _calculate_number_of_increases(measurements: list, selection_strategy: Callable) -> int:
    previous = None
    increases = 0

    for idx in range(len(measurements)):
        value = selection_strategy(idx)
        if previous is not None and value > previous:
            increases += 1
        previous = value

    return increases


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
