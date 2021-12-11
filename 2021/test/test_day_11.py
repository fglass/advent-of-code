from solution.day_11 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 1656
    assert part1(INPUT) == 1702


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 195
    assert part2(INPUT) == 251
