from solution.day_7 import part1, part2, INPUT

EXAMPLE_INPUT = "16,1,2,0,4,2,7,1,2,14"


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 37
    assert part1(INPUT) == 344297


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 168
    assert part2(INPUT) == 97164301
