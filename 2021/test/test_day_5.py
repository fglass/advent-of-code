from solution.day_5 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 5
    assert part1(INPUT) == 6007


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 12
    assert part2(INPUT) == 19349
