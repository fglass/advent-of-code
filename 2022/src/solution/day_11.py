import math
from collections import deque
from input_loader import load_input_lines
from typing import List

INPUT = load_input_lines(day=11)
NOTES_PER_MONKEY = 7
N_ACTIVE_MONKEYS = 2


class Monkey:
    def __init__(self, items: List[int], raw_operation: str, test_divisor: int, true_target: int, false_target: int):
        self.items = deque(items)
        self.raw_operation = raw_operation
        self.test_divisor = test_divisor
        self.true_target = true_target
        self.false_target = false_target
        self.inspects = 0

    @staticmethod
    def init(notes: List[str], note_idx: int):
        return Monkey(
            items=_parse_starting_items(notes[note_idx + 1]),
            raw_operation=_parse_operation(notes[note_idx + 2]),
            test_divisor=_parse_last_int(notes[note_idx + 3]),
            true_target=_parse_last_int(notes[note_idx + 4]),
            false_target=_parse_last_int(notes[note_idx + 5]),
        )

    def catch(self, item: int):
        self.items.append(item)

    def inspect_items(self, worry_relief: int, worry_limit: int) -> iter:
        while len(self.items) > 0:
            item = self.items.popleft()
            inspected_item = self._inspect_item(item)
            inspected_item = (inspected_item // worry_relief) % worry_limit
            yield inspected_item, self._get_target(inspected_item)

    def _inspect_item(self, item: int) -> int:
        self.inspects += 1
        return eval(self.raw_operation)

    def _get_target(self, item: int) -> int:
        test_success = item % self.test_divisor == 0
        return self.true_target if test_success else self.false_target


def part1(notes: List[str]) -> int:
    monkeys = _initialise_monkeys(notes)
    _play_keep_away(monkeys, rounds=20, worry_relief=3)
    return _calculate_monkey_business(monkeys)


def part2(notes: List[str]) -> int:
    monkeys = _initialise_monkeys(notes)
    _play_keep_away(monkeys, rounds=10_000, worry_relief=1)
    return _calculate_monkey_business(monkeys)


def _initialise_monkeys(notes: List[str]) -> List[Monkey]:
    return [Monkey.init(notes, i) for i in range(0, len(notes), NOTES_PER_MONKEY)]


def _play_keep_away(monkeys: List[Monkey], rounds: int, worry_relief: int):
    worry_limit = math.prod(m.test_divisor for m in monkeys)
    for _ in range(rounds):
        _play_round(monkeys, worry_relief, worry_limit)


def _play_round(monkeys: List[Monkey], worry_relief: int, worry_limit: int):
    for monkey in monkeys:
        for item, target in monkey.inspect_items(worry_relief, worry_limit):
            monkeys[target].catch(item)


def _calculate_monkey_business(monkeys: List[Monkey]) -> int:
    max_inspects = sorted((m.inspects for m in monkeys), reverse=True)[:N_ACTIVE_MONKEYS]
    return math.prod(max_inspects)


def _parse_starting_items(note: str) -> List[int]:
    return [int(x) for x in note[18:].split(",")]


def _parse_operation(note: str) -> str:
    return note[19:].replace("old", "item")


def _parse_last_int(note: str) -> int:
    return int(note.split()[-1])


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
