from input_loader import load_input_lines

INPUT = load_input_lines(day=14)


def part1(lines: list) -> int:
    return _run_polymerisation(lines, steps=10)


def part2(lines: list) -> int:
    return _run_polymerisation(lines, steps=40)


def _run_polymerisation(lines: list, steps: int):
    polymer_template, insertion_rules = _parse_lines(lines)
    pairs = _init_pairs(polymer_template)

    for _ in range(steps):
        pairs = _polymerise(pairs, insertion_rules)

    return _calculate_result(pairs, last_letter=polymer_template[-1])


def _parse_lines(lines: list) -> tuple:
    polymer_template = lines[0]
    insertion_rules = {}

    for line in lines[2:]:
        pair, target = line.split(" -> ")
        insertion_rules[pair] = target

    return polymer_template, insertion_rules


def _init_pairs(polymer_template: str) -> dict:
    pairs = {}

    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i] + polymer_template[i + 1]
        pairs[pair] = pairs.get(pair, 0) + 1

    return pairs


def _polymerise(pairs: dict, insertion_rules: dict) -> dict:
    new_pairs = {}

    for pair, frequency in pairs.items():
        target = insertion_rules[pair]
        for p in (pair[0] + target, target + pair[1]):
            new_pairs[p] = new_pairs.get(p, 0) + frequency

    return new_pairs


def _calculate_result(pairs: dict, last_letter: str) -> int:
    letters = {}

    for pair, frequency in pairs.items():
        letters[pair[0]] = letters.get(pair[0], 0) + frequency

    letters[last_letter] += 1
    frequencies = sorted(letters.values())

    return frequencies[-1] - frequencies[0]


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
