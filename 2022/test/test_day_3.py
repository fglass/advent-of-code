from solution.day_3 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 157
    assert part1(INPUT) == 7908


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 70
    assert part2(INPUT) == 2838
