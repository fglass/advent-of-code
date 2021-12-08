from input_loader import load_input_lines

INPUT = load_input_lines(day=8)

RULES = {
    0: lambda pattern, results: len(pattern) == 6,
    1: lambda pattern, results: len(pattern) == 2,
    2: lambda pattern, results: pattern,
    3: lambda pattern, results: len(pattern) == 5 and len(pattern.intersection(results[1])) == 2,
    4: lambda pattern, results: len(pattern) == 4,
    5: lambda pattern, results: len(pattern) == 5 and len(pattern.intersection(results[6])) == 5,
    6: lambda pattern, results: len(pattern) == 6 and len(pattern.intersection(results[1])) == 1,
    7: lambda pattern, results: len(pattern) == 3,
    8: lambda pattern, results: len(pattern) == 7,
    9: lambda pattern, results: pattern == results[4].union(results[3])
}


def part1(notes: list) -> int:
    rule_order = [1, 4, 7, 8]
    total_appearances = 0

    for signal_patterns, output_values in _parse_notes(notes):
        lookup = _apply_rules(signal_patterns, rule_order)
        total_appearances += len([value for value in output_values if value in lookup])

    return total_appearances


def part2(notes: list) -> int:
    rule_order = [1, 4, 7, 8, 6, 3, 9, 5, 0, 2]
    total_output = 0

    for signal_patterns, output_values in _parse_notes(notes):
        results = _apply_rules(signal_patterns, rule_order)
        output = "".join(map(lambda value: str(results[value]), output_values))
        total_output += int(output)

    return total_output


def _apply_rules(signal_patterns: list, rule_order: list) -> dict:
    results = {}

    for idx in rule_order:
        rule_fn = RULES[idx]
        result = next(filter(lambda pattern: rule_fn(pattern, results), signal_patterns))
        results[idx] = result
        signal_patterns.remove(result)

    return {"".join(sorted(v)): k for k, v in results.items()}


def _parse_notes(notes: list) -> tuple:
    for entry in notes:
        _input, output = entry.split(" | ")
        signal_patterns = [set(pattern) for pattern in _input.split()]
        output_values = ["".join(sorted(value)) for value in output.split()]
        yield signal_patterns, output_values


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
