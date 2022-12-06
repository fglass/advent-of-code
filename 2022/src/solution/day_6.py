from input_loader import load_input_line

INPUT = load_input_line(day=6)


def part1(stream: str) -> int:
    return _find_marker_end(stream, size=4)


def part2(stream: str) -> int:
    return _find_marker_end(stream, size=14)


def _find_marker_end(stream: str, size: int) -> int:
    start = 0
    window = set()

    for idx, char in enumerate(stream):
        while char in window:
            window.remove(stream[start])
            start += 1

        window.add(char)

        if len(window) == size:
            return idx + 1

    return -1


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
