import functools
import json
from input_loader import load_input_lines
from typing import List, Union

INPUT = load_input_lines(day=13)
DIVIDER_PACKETS = [[[6]], [[2]]]
LESS_THAN, EQUAL, GREATER_THAN = -1, 0, 1


def part1(lines: List[str]) -> int:
    indices_sum = 0
    pair_idx = 1

    for i in range(0, len(lines), 3):
        left = json.loads(lines[i])
        right = json.loads(lines[i + 1])

        if _compare_packets(left, right) == LESS_THAN:
            indices_sum += pair_idx

        pair_idx += 1

    return indices_sum


def part2(lines: List[str]) -> int:
    packets = list(DIVIDER_PACKETS)

    for line in lines:
        if line != "":
            packet = json.loads(line)
            packets.append(packet)

    packets.sort(key=functools.cmp_to_key(_compare_packets))

    return _calculate_decoder_key(packets)


def _compare_packets(left: list, right: list) -> int:
    for i in range(len(left)):
        if i >= len(right):
            return GREATER_THAN

        left_val = left[i]
        right_val = right[i]

        if left_val == right_val:
            continue
        elif isinstance(left_val, int) and isinstance(right_val, int):
            return LESS_THAN if left_val < right_val else GREATER_THAN
        else:
            return _compare_packets(_to_list(left_val), _to_list(right_val))

    return LESS_THAN if len(left) < len(right) else EQUAL


def _calculate_decoder_key(packets: list) -> int:
    decoder_key = 1

    for divider in DIVIDER_PACKETS:
        decoder_key *= packets.index(divider) + 1

    return decoder_key


def _to_list(val: Union[int, list]) -> list:
    return [val] if isinstance(val, int) else val


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
