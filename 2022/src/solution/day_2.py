from input_loader import load_input_lines
from typing import List, Callable

INPUT = load_input_lines(day=2)

ROCK, PAPER, SCISSORS = "A", "B", "C"
WIN, DRAW, LOSS = 6, 3, 0

SHAPE_MAPPING = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
SHAPE_SCORES = {ROCK: 1, PAPER: 2, SCISSORS: 3}

OUTCOME_MAPPING = {"X": LOSS, "Y": DRAW, "Z": WIN}
OUTCOME_SCORES = {
    ROCK: {SCISSORS: LOSS, ROCK: DRAW, PAPER: WIN},
    PAPER: {ROCK: LOSS, PAPER: DRAW, SCISSORS: WIN},
    SCISSORS: {PAPER: LOSS, SCISSORS: DRAW, ROCK: WIN}
}
OUTCOME_SCORES_REV = {k: {v2: k2 for k2, v2 in v.items()} for k, v in OUTCOME_SCORES.items()}


def part1(rounds: List[str]) -> int:

    def score_round(p1: str, p2_raw: str) -> int:
        p2 = SHAPE_MAPPING[p2_raw]
        outcome_score = OUTCOME_SCORES[p1][p2]
        return SHAPE_SCORES[p2] + outcome_score

    return _calculate_score(rounds, score_strategy=score_round)


def part2(rounds: List[str]) -> int:

    def score_round(p1: str, outcome: str) -> int:
        outcome_score = OUTCOME_MAPPING[outcome]
        p2 = OUTCOME_SCORES_REV[p1][outcome_score]
        return SHAPE_SCORES[p2] + outcome_score

    return _calculate_score(rounds, score_strategy=score_round)


def _calculate_score(rounds: List[str], score_strategy: Callable) -> int:
    return sum(score_strategy(a, b) for a, _, b in rounds)


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
