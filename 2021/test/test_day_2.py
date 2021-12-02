from solution.day_2 import part1, part2, INPUT

EXAMPLE_INPUT = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 150
    assert part1(INPUT) == 2120749


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 900
    assert part2(INPUT) == 2138382217
