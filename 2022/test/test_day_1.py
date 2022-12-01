from solution.day_1 import part1, part2, INPUT

EXAMPLE_INPUT = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 24000
    assert part1(INPUT) == 72511


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 45000
    assert part2(INPUT) == 212117
