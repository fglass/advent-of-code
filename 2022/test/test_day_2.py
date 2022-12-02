from solution.day_2 import part1, part2, INPUT

EXAMPLE_INPUT = ["A Y", "B X", "C Z"]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 15
    assert part1(INPUT) == 8890


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 12
    assert part2(INPUT) == 10238
