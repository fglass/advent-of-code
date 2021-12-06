from input_loader import load_input_line

INPUT = load_input_line(day=6)
NEW_CYCLE_AGE = 6
FIRST_CYCLE_AGE = NEW_CYCLE_AGE + 2


def part1(initial_ages: str) -> int:
    return _simulate_growth(initial_ages, days=80)


def part2(initial_ages: str) -> int:
    return _simulate_growth(initial_ages, days=256)


def _simulate_growth(initial_ages: str, days: int) -> int:
    fish_by_ages = _initialise_state(initial_ages)
    [_tick(fish_by_ages) for _ in range(days)]
    return sum(fish_by_ages.values())


def _initialise_state(initial_ages: str) -> dict:
    fish_by_ages = {}

    for n in initial_ages.split(","):
        age = int(n)
        fish_by_ages[age] = fish_by_ages.get(age, 0) + 1

    return fish_by_ages


def _tick(fish_by_ages: dict):
    previous_fish = 0

    for i in range(FIRST_CYCLE_AGE, -1, -1):
        fish = fish_by_ages.get(i, 0)
        fish_by_ages[i] = previous_fish
        previous_fish = fish

        if i == 0:
            fish_by_ages[NEW_CYCLE_AGE] += fish
            fish_by_ages[FIRST_CYCLE_AGE] = fish


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
