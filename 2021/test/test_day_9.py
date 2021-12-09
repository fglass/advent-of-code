from solution.day_9 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 15
    assert part1(INPUT) == 486


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 1134
    assert part2(INPUT) == 1059300
