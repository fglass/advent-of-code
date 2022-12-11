from input_loader import load_input_lines
from typing import List

INPUT = load_input_lines(day=10)
TARGET_CYCLES = {20, 60, 100, 140, 180, 220}
CRT_WIDTH = 40


def part1(instructions: List[str]) -> int:
    register = cycle = 1
    signal_strength_sum = 0

    def _on_cycle() -> int:
        return cycle * register if cycle in TARGET_CYCLES else 0

    for instruction in instructions:
        if instruction.startswith("addx"):
            cycle += 1
            signal_strength_sum += _on_cycle()
            register += _get_value(instruction)

        cycle += 1
        signal_strength_sum += _on_cycle()

    return signal_strength_sum


def part2(instructions: List[str]) -> List[List[str]]:
    crt_x = 0
    register = 1
    image = []

    def _on_cycle() -> int:
        if crt_x == 0:
            image.append([])

        is_lit = abs(crt_x - register) <= 1
        pixel = "#" if is_lit else "."
        image[-1].append(pixel)

        return (crt_x + 1) % CRT_WIDTH

    for instruction in instructions:
        if instruction.startswith("noop"):
            crt_x = _on_cycle()
        elif instruction.startswith("addx"):
            crt_x = _on_cycle()
            crt_x = _on_cycle()
            register += _get_value(instruction)

    return image


def _get_value(instruction: str) -> int:
    return int(instruction.split()[1])


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    for row in part2(INPUT):
        print(" ".join(row))
