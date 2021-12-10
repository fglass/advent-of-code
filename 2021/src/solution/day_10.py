from input_loader import load_input_lines

INPUT = load_input_lines(day=10)

CHAR_MAPPING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def part1(lines: list) -> int:
    total_score = 0

    for line in lines:
        invalid_char, _ = _parse_line(line)
        if invalid_char is not None:
            total_score += SCORES[invalid_char]

    return total_score


def part2(lines: list) -> int:
    total_scores = []

    for line in lines:
        _, stack = _parse_line(line)
        if stack is not None:
            total_scores.append(_calculate_completion_score(stack))

    median_idx = int(len(total_scores) / 2)
    return sorted(total_scores)[median_idx]


def _parse_line(line: str) -> tuple:
    stack = []

    for char in line:
        if char in CHAR_MAPPING.keys():
            closed_char = CHAR_MAPPING[char]
            stack.append(closed_char)
        elif char != stack.pop():
            return char, None

    return None, stack


def _calculate_completion_score(stack: list):
    score_multiplier = 5
    total_score = 0

    for _ in range(len(stack)):
        next_char = stack.pop()
        score = list(SCORES).index(next_char) + 1
        total_score = total_score * score_multiplier + score

    return total_score


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
