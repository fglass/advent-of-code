from solution.day_6 import part1, part2, INPUT

EXAMPLE_INPUT = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 7
    assert part1(INPUT) == 1707


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 19
    assert part2(INPUT) == 3697
