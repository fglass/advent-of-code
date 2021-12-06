from solution.day_6 import part1, part2, INPUT

EXAMPLE_INPUT = "3,4,3,1,2"


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 5934
    assert part1(INPUT) == 371379


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 26984457539
    assert part2(INPUT) == 1674303997472
