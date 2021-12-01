from solution.day_1 import part1, part2, INPUT

EXAMPLE_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 7
    assert part1(INPUT) == 1298


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 5
    assert part2(INPUT) == 1248
