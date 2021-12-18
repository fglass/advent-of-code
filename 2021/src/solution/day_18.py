from math import floor, ceil
from input_loader import load_input_lines

INPUT = load_input_lines(day=18)
EXPLODE_THRESHOLD = 4
SPLIT_THRESHOLD = 10


def part1(numbers: list) -> int:
    result = _flatten(numbers[0])

    for i in range(1, len(numbers)):
        result = _add(result, _flatten(numbers[i]))

    return _calculate_magnitude(result)


def part2(numbers: list) -> int:
    result = 0

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            ij = _add(_flatten(numbers[i]), _flatten(numbers[j]))
            ji = _add(_flatten(numbers[j]), _flatten(numbers[i]))
            result = max(result, _calculate_magnitude(ij), _calculate_magnitude(ji))

    return result


def _flatten(number: str) -> list:
    flattened = []
    depth = 0

    for char in number[1:-1].replace(",", ""):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        else:
            flattened.append([int(char), depth])

    return flattened


def _add(n1: list, n2: list) -> list:
    paired = [[v, d + 1] for [v, d] in n1 + n2]
    return _reduce(paired)


def _reduce(n: list) -> list:
    exploded, split = (True, False)

    while exploded or split:
        n, exploded = _explode(n)
        if not exploded:
            n, split = _split(n)

    return n


def _explode(n: list) -> tuple:
    for idx in range(len(n) - 1):
        v1, d1 = n[idx]
        v2, d2 = n[idx + 1]

        if d1 == d2 and d1 == EXPLODE_THRESHOLD:
            if idx > 0:
                n[idx - 1][0] += v1
            if idx < len(n) - 2:
                n[idx + 2][0] += v2

            del n[idx:idx + 2]
            n.insert(idx, [0, d1 - 1])

            return n, True

    return n, False


def _split(n: list) -> tuple:
    for idx in range(len(n)):
        v, d = n[idx]

        if v >= SPLIT_THRESHOLD:
            halved = v / 2
            del n[idx]
            n.insert(idx, [ceil(halved), d + 1])
            n.insert(idx, [floor(halved), d + 1])
            return n, True

    return n, False


def _calculate_magnitude(n: list) -> int:
    while len(n) > 1:

        for idx in range(len(n) - 1):
            v1, d1 = n[idx]
            v2, d2 = n[idx + 1]

            if d1 == d2:
                new_value = v1 * 3 + v2 * 2

                del n[idx:idx + 2]
                n.insert(idx, [new_value, d1 - 1])
                break

    return n[0][0]


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
