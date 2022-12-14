from solution.day_14 import part1, part2, INPUT

EXAMPLE_INPUT = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9",]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 24
    assert part1(INPUT) == 672


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 93
    assert part2(INPUT) == 26831
