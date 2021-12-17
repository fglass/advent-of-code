from solution.day_17 import part1, part2, INPUT

EXAMPLE_INPUT = "target area: x=20..30, y=-10..-5"


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 45
    assert part1(INPUT) == 12561


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 112
    assert part2(INPUT) == 3785
