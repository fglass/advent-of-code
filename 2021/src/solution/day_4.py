from input_loader import load_input_lines
from typing import Generator

INPUT = load_input_lines(day=4)
GRID_SIZE = 5


def part1(puzzle_input: list) -> int:
    winning_score = next(_play_bingo(puzzle_input))
    return winning_score


def part2(puzzle_input: list) -> int:
    losing_score = list(_play_bingo(puzzle_input))[-1]
    return losing_score


def _play_bingo(puzzle_input: list) -> Generator:
    all_numbers = _parse_numbers(puzzle_input[0])
    boards = _create_boards(puzzle_input[1:])

    for i in range(GRID_SIZE, len(all_numbers) + 1):
        drawn_numbers = all_numbers[:i]
        for board in boards:
            if _has_bingo(board, drawn_numbers):
                boards.remove(board)
                yield _calculate_score(board, drawn_numbers)


def _parse_numbers(line: str) -> list:
    return [int(n) for n in line.split(",")]


def _create_boards(boards_input: list) -> list:
    boards = []

    for i in range(1, len(boards_input), GRID_SIZE + 1):
        board_input = boards_input[i:i+GRID_SIZE]
        boards.append(_create_board(board_input))

    return boards


def _create_board(board_input: list) -> list:
    return [_parse_board_row(row) for row in board_input]


def _parse_board_row(row: str) -> list:
    return [int(number.strip()) for number in row.split(" ") if number != ""]


def _has_bingo(board: list, drawn_numbers: list) -> bool:
    matching_row = any(_is_matching_axis(row, drawn_numbers) for row in board)
    matching_column = any(_is_matching_axis(column, drawn_numbers) for column in zip(*board))
    return matching_row or matching_column


def _is_matching_axis(axis: iter, drawn_numbers: list) -> bool:
    return all(number in drawn_numbers for number in axis)


def _calculate_score(board: list, drawn_numbers: list) -> int:
    last_drawn = drawn_numbers[-1]
    unmarked_numbers = [number for row in board for number in row if number not in drawn_numbers]
    return last_drawn * sum(unmarked_numbers)


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
