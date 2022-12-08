from solution.day_8 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 21
    assert part1(INPUT) == 1543


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 8
    assert part2(INPUT) == 595080
