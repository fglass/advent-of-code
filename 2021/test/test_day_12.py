from solution.day_12 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]

EXAMPLE_INPUT_2 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 10
    assert part1(EXAMPLE_INPUT_2) == 226
    assert part1(INPUT) == 5958


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 36
    assert part2(EXAMPLE_INPUT_2) == 3509
    assert part2(INPUT) == 150426
