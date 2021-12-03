from solution.day_3 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 198
    assert part1(INPUT) == 2972336


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 230
    assert part2(INPUT) == 3368358
