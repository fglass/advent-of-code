from solution.day_13 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "[1, 1, 3, 1, 1]",
    "[1, 1, 5, 1, 1]",
    "",
    "[[1], [2, 3, 4]]",
    " [[1], 4]",
    "",
    "[9]",
    "[[8, 7, 6]]",
    "",
    "[[4, 4], 4, 4]",
    "[[4, 4], 4, 4, 4]",
    "",
    "[7, 7, 7, 7]",
    "[7, 7, 7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]",
    "[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 13
    assert part1(INPUT) == 6395


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 140
    assert part2(INPUT) == 24921
