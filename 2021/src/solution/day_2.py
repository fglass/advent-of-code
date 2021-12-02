from typing import Generator
from input_loader import load_input_lines

INPUT = load_input_lines(day=2)
FORWARD = "forward"
DOWN = "down"
UP = "up"


def part1(commands: list) -> int:
    horizontal = depth = 0

    for (direction, magnitude) in _parse_commands(commands):
        if direction == FORWARD:
            horizontal += magnitude
        elif direction == DOWN:
            depth += magnitude
        elif direction == UP:
            depth -= magnitude

    return horizontal * depth


def part2(commands: list) -> int:
    horizontal = depth = aim = 0

    for (direction, magnitude) in _parse_commands(commands):
        if direction == FORWARD:
            horizontal += magnitude
            depth += (magnitude * aim)
        elif direction == DOWN:
            aim += magnitude
        elif direction == UP:
            aim -= magnitude

    return horizontal * depth


def _parse_commands(commands: list) -> Generator:
    for command in commands:
        direction, magnitude = command.split(" ")
        yield direction, int(magnitude)


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
