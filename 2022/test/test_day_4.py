from solution.day_4 import part1, part2, INPUT

EXAMPLE_INPUT = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 2
    assert part1(INPUT) == 536


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 4
    assert part2(INPUT) == 845
