from functools import reduce
from input_loader import load_input_lines
from typing import List

INPUT = load_input_lines(day=3)


def part1(rucksacks: List[str]) -> int:
    total_priority = 0

    for rucksack in rucksacks:
        mid_pt = len(rucksack) // 2
        halves = [rucksack[:mid_pt], rucksack[mid_pt:]]
        common_item = _get_common_item(halves)
        total_priority += _get_priority(common_item)

    return total_priority


def part2(rucksacks: List[str], group_size: int = 3) -> int:
    total_priority = 0

    for idx in range(0, len(rucksacks), group_size):
        group = [rucksacks[idx + i] for i in range(group_size)]
        common_item = _get_common_item(group)
        total_priority += _get_priority(common_item)

    return total_priority


def _get_common_item(sequence: iter) -> str:
    return reduce(lambda a, b: set(a) & set(b), sequence).pop()


def _get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 1 + 26


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
