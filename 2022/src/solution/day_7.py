from input_loader import load_input_lines
from typing import List, Dict, Union, Callable

INPUT = load_input_lines(day=7)
Directory = Dict[str, Union[int, dict]]

MAX_DIR_SIZE = 100_000
MAX_DISK_SPACE = 70_000_000
UPDATE_DISK_SPACE = 30_000_000


def part1(terminal_output: List[str]) -> int:
    dir_sizes = _get_dir_sizes(terminal_output)
    return sum(size for size in dir_sizes if size <= MAX_DIR_SIZE)


def part2(terminal_output: List[str]) -> int:
    dir_sizes = _get_dir_sizes(terminal_output)
    used_space = dir_sizes[-1]
    return min(size for size in dir_sizes if _can_update(used_space, size))


def _get_dir_sizes(terminal_output: List[str]) -> List[int]:
    root_dir = _build_file_system(terminal_output)

    dir_sizes = []
    _walk_file_system(root_dir, on_directory_size=lambda size: dir_sizes.append(size))

    return dir_sizes


def _build_file_system(terminal_output: List[str]) -> Directory:
    root_dir = {}
    path = []

    for line in terminal_output:

        if line[0].isdigit():
            size, filename = line.split()
            path[-1][filename] = int(size)

        elif line.startswith("$ cd"):
            arg = line.split()[-1]
            if arg == "/":
                path = [root_dir]
            elif arg == "..":
                path.pop()
            else:
                new_dir = {}
                path[-1][arg] = new_dir
                path.append(new_dir)

    return root_dir


def _walk_file_system(directory: Directory, on_directory_size: Callable) -> int:
    size = 0

    for child in directory.values():
        if isinstance(child, dict):
            size += _walk_file_system(child, on_directory_size)
        else:
            size += child

    on_directory_size(size)

    return size


def _can_update(used_space: int, reclaimed_space: int) -> bool:
    return used_space - reclaimed_space + UPDATE_DISK_SPACE <= MAX_DISK_SPACE


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
