from input_loader import load_input_line

INPUT = load_input_line(day=17)


def part1(line: str) -> int:
    _, _, min_y, _ = _get_target_area(line)
    return int((min_y * (min_y + 1)) / 2)


def part2(line: str) -> int:
    target_area = _get_target_area(line)
    _, max_x, min_y, _ = target_area

    hits = 0

    for x in range(max_x + 1):
        for y in range(min_y, abs(min_y) + 1):
            if _fire_probe(target_area, velocity=(x, y)):
                hits += 1

    return hits


def _get_target_area(line: str) -> tuple:
    bounds = line[15:].split(", y=")
    (min_x, max_x), (min_y, max_y) = [bound.split("..") for bound in bounds]
    return int(min_x), int(max_x), int(min_y), int(max_y)


def _fire_probe(target_area: tuple, velocity: tuple) -> bool:
    min_x, max_x, min_y, max_y = target_area
    vx, vy = velocity
    x, y = (0, 0)

    while y > min_y:
        x, y = (x + vx, y + vy)

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True

        vx, vy = (vx - 1 if vx > 0 else vx, vy - 1)

    return False


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
