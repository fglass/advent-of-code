from solution.day_14 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 1588
    assert part1(INPUT) == 2947


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 2188189693529
    assert part2(INPUT) == 3232426226464
