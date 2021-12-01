from typing import List


def load_file(day: int) -> List[int]:
    with open(f"res/day{day}.txt") as f:
        return [int(line.replace("\n", "")) for line in f.readlines()]
