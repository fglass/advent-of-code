from input_loader import load_input_lines
from typing import List

INPUT = load_input_lines(day=10)
TARGET_CYCLES = {20, 60, 100, 140, 180, 220}
CRT_WIDTH = 39
SPRITE_WIDTH = 3


def part1(instructions: List[str]) -> int:
    register = cycle = 1
    signal_strength_sum = 0

    for instruction in instructions:

        if instruction.startswith("addx"):
            cycle += 1
            if cycle in TARGET_CYCLES:
                signal_strength_sum += cycle * register

            register += _get_value(instruction)

        cycle += 1
        if cycle in TARGET_CYCLES:
            signal_strength_sum += cycle * register

    return signal_strength_sum


def part2(instructions: List[str]):
    for row in _produce_image(instructions):
        print(" ".join(row))


def _produce_image(instructions: List[str]) -> List[List[str]]:
    register = 1
    crt_pos = 0
    image = [["#"]]

    def _on_cycle(next_crt_pos: int):
        pixel = "#" if abs(next_crt_pos - register) < SPRITE_WIDTH - 1 else "."
        image[-1].append(pixel)

        if next_crt_pos == CRT_WIDTH:
            image.append([])
            return -1

        return next_crt_pos

    for instruction in instructions:

        if instruction.startswith("addx"):
            crt_pos = _on_cycle(crt_pos + 1)
            register += _get_value(instruction)

        crt_pos = _on_cycle(crt_pos + 1)

    return image


def _get_value(instruction: str) -> int:
    return int(instruction.split()[1])


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    part2(INPUT)  # Prints "BGKAEREZ"
