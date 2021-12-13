import functools
import sys
from input_loader import load_input_lines

INPUT = load_input_lines(day=13)


def part1(puzzle_input: list) -> int:
    dots, folds = _init(puzzle_input)
    dots = _fold_paper(dots, folds[0])
    return len(dots)


def part2(puzzle_input: list) -> int:
    dots, folds = _init(puzzle_input)

    for fold in folds:
        dots = _fold_paper(dots, fold)

    _pretty_print(dots)
    return len(dots)


def _init(puzzle_input: list) -> tuple:
    dots = set()
    folds = []

    def parse_position(position: str):
        x, y = position.split(",")
        dots.add((int(x), int(y)))

    def parse_instruction(instruction: str):
        axis, n = instruction.replace("fold along ", "").split("=")
        folds.append((axis, int(n)))

    parse_strategy = parse_position

    for line in puzzle_input:
        if line == "":
            parse_strategy = parse_instruction
        else:
            parse_strategy(line)

    return dots, folds


def _fold_paper(dots: set, fold: tuple) -> set:
    new_dots = set()
    axis, n = fold
    coord_idx = 0 if axis == "x" else 1

    for dot in dots:
        value = dot[coord_idx]
        is_unchanged = value <= n

        if is_unchanged:
            new_dots.add(dot)
            continue

        new_dot = list(dot)
        new_dot[coord_idx] = n - (value - n)
        new_dots.add(tuple(new_dot))

    return new_dots


def _pretty_print(dots: set):
    min_y, max_y, min_x, max_x = _minmax(dots)

    for y in range(min_y, max_y + 1):
        print("")
        for x in range(min_x, max_x + 1):
            char = "#" if (x, y) in dots else "."
            print(char, " ", end="")


def _minmax(dots: set) -> tuple:
    return functools.reduce(
        lambda acc, dot: (min(acc[0], dot[1]), max(acc[1], dot[1]), min(acc[2], dot[0]), max(acc[3], dot[0])),
        dots,
        (sys.maxsize, 0, sys.maxsize, 0)
    )


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
