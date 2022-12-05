import re
from collections import deque
from input_loader import load_input_lines

INPUT = load_input_lines(day=5)
STACK_SPACING = 4
CRATE_PATTERN = r"\w\]"
STEP_PATTERN = r"move (\d+) from (\d+) to (\d+)"


def part1(lines: list) -> str:
    return _run_procedure(lines)


def part2(lines: list) -> str:
    return _run_procedure(lines, multi=True)


def _run_procedure(lines: list, multi: bool = False) -> str:
    stacks, procedure = _parse_input(lines)
    _do_steps(procedure, stacks, multi)
    return _get_stack_heads(stacks)


def _parse_input(lines: list) -> tuple:
    split_idx = lines.index("")
    stack_rows = lines[:split_idx]
    raw_steps = lines[split_idx + 1:]
    return _parse_drawing_input(stack_rows), _parse_procedure_input(raw_steps)


def _do_steps(procedure: list, stacks: list, multi: bool):
    for quantity, src, dest in procedure:
        crane = [stacks[src].pop() for _ in range(quantity)]

        if multi:
            crane.reverse()

        for crate in crane:
            stacks[dest].append(crate)


def _get_stack_heads(stacks: list) -> str:
    return "".join(stack[-1] for stack in stacks if len(stack) > 0)


def _parse_drawing_input(rows: list) -> list:
    stacks = []

    for row in rows:
        for match in re.finditer(CRATE_PATTERN, row):
            crate_idx = match.start()
            stack_idx = crate_idx // STACK_SPACING

            while len(stacks) <= stack_idx:
                stacks.append(deque())

            crate = row[crate_idx]
            stacks[stack_idx].appendleft(crate)

    return stacks


def _parse_procedure_input(steps: list) -> list:
    matches = (re.match(STEP_PATTERN, step).groups() for step in steps)
    return [(int(quantity), int(src) - 1, int(dest) - 1) for quantity, src, dest in matches]


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
