import operator
from input_loader import load_input_lines
from typing import Callable

INPUT = load_input_lines(day=3)


def part1(report: list) -> int:
    gamma_rate = ""

    for column in zip(*report):
        most_common_bit = _resolve_target_bit(column, bit_criteria=operator.ge)
        gamma_rate += most_common_bit

    epsilon_rate = _flip_bits(gamma_rate)

    return _to_decimal(gamma_rate) * _to_decimal(epsilon_rate)


def part2(report: list) -> int:
    o2_rating = _calculate_gas_rating(report, bit_criteria=operator.ge)
    co2_rating = _calculate_gas_rating(report, bit_criteria=operator.lt)
    return o2_rating * co2_rating


def _calculate_gas_rating(report: list, bit_criteria: Callable) -> int:
    kept_positions = range(len(report))

    for column in zip(*report):
        if len(kept_positions) == 1:
            break

        column = [bit for position, bit in enumerate(column) if position in kept_positions]
        target_bit = _resolve_target_bit(column, bit_criteria)
        selected_positions = []

        for idx, bit in enumerate(column):
            if bit == target_bit:
                position = kept_positions[idx]
                selected_positions.append(position)

        kept_positions = selected_positions

    rating = report[kept_positions[0]]

    return _to_decimal(rating)


def _resolve_target_bit(column: iter, bit_criteria: Callable) -> str:
    n_ones = column.count("1")
    max_frequency = len(column) / 2
    return "1" if bit_criteria(n_ones, max_frequency) else "0"


def _flip_bits(binary_string: str) -> str:
    return "".join("0" if bit == "1" else "1" for bit in binary_string)


def _to_decimal(binary_string: str) -> int:
    return int(binary_string, 2)


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
