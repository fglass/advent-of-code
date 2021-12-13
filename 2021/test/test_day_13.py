from solution.day_13 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 17
    assert part1(INPUT) == 737


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 16
    assert part2(INPUT) == 96
