from typing import List, Iterator


def load_input_line(day: int) -> str:
    return next(_generate_lines(day))


def load_input_lines(day: int) -> List[str]:
    return list(_generate_lines(day))


def load_input_sequence(day: int) -> List[int]:
    return [int(line) for line in _generate_lines(day)]


def _generate_lines(day: int) -> Iterator[str]:
    with open(f"res/day{day}.txt") as f:
        for line in f.readlines():
            yield line.rstrip("\n")
