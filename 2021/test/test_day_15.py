from solution.day_15 import part1, part2, INPUT

EXAMPLE_INPUT = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581"
]


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 40
    assert part1(INPUT) == 745


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 315
    assert part2(INPUT) == 3002
