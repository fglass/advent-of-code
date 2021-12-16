from solution.day_16 import part1, part2, INPUT

EXAMPLE_INPUT = "8A004A801A8002F478"
EXAMPLE_INPUT_2 = "9C0141080250320F1802104A08"


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 16
    assert part1(INPUT) == 871


def test_part_2():
    assert part2(EXAMPLE_INPUT_2) == 1
    assert part2(INPUT) == 68703010504
