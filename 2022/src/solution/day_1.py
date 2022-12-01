import heapq
from input_loader import load_input_lines
from typing import List

INPUT = load_input_lines(day=1)


def part1(item_list: List[str]) -> int:
    return _get_top_elves(item_list, k=1)[0]


def part2(item_list: List[str]) -> int:
    return sum(_get_top_elves(item_list, k=3))


def _get_top_elves(item_list: List[str], k: int) -> List[int]:  # O(nlogk) time
    min_heap = []
    n_calories = 0

    for line in item_list:

        if line.isnumeric():
            n_calories += int(line)

        if line == "" or line == item_list[-1]:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n_calories)
            else:
                heapq.heappushpop(min_heap, n_calories)

            n_calories = 0

    return min_heap


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
