from solution.day_5 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "    [D]",
    "[N] [C]",
    "[Z] [M] [P]",
    " 1   2   3",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == "CMZ"
    assert part1(INPUT) == "LJSVLTWQM"


def test_part_2():
    assert part2(EXAMPLE_INPUT) == "MCD"
    assert part2(INPUT) == "BRQWDBBJM"
