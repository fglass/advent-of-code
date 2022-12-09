from solution.day_9 import part1, part2, INPUT

EXAMPLE_INPUT = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
EXAMPLE_INPUT_2 = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 13
    assert part1(INPUT) == 6197


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 1
    assert part2(EXAMPLE_INPUT_2) == 36
    assert part2(INPUT) == 2562
