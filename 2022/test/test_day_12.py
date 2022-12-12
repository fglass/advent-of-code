from solution.day_12 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 31
    assert part1(INPUT) == 352


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 29
    assert part2(INPUT) == 345
