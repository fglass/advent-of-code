from input_loader import load_input_lines
from typing import Optional

INPUT = load_input_lines(day=12)


def part1(lines: list) -> int:
    graph = _build_graph(lines)
    all_paths = _traverse_graph(graph, current_path=["start"], twice_node=None)
    return len(all_paths)


def part2(lines: list) -> int:
    all_paths = set()
    graph = _build_graph(lines)
    small_nodes = filter(lambda node: node == node.lower() and len(node) <= 2, graph)

    for small_node in small_nodes:
        for path in _traverse_graph(graph, current_path=["start"], twice_node=small_node):
            path = tuple(path)
            if path not in all_paths:
                all_paths.add(path)

    return len(all_paths)


def _build_graph(lines: list) -> dict:
    graph = {}

    for line in lines:
        src, dest = line.split("-")
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)

    return graph


def _traverse_graph(graph: dict, current_path: list, twice_node: Optional[str]):
    all_paths = []
    node = current_path[-1]

    for neighbour in graph[node]:
        new_path = current_path.copy()

        is_small_node = neighbour.islower()
        visited_small_node = is_small_node and neighbour in new_path
        can_visit_twice = is_small_node and neighbour == twice_node and current_path.count(twice_node) < 2

        if neighbour == "start" or (visited_small_node and not can_visit_twice):
            continue

        new_path.append(neighbour)

        if neighbour == "end":
            all_paths.append(new_path)
            continue

        all_paths.extend(_traverse_graph(graph, new_path, twice_node))

    return all_paths


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
