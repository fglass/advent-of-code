import functools
import heapq
import math
from input_loader import load_input_lines

INPUT = load_input_lines(day=15)


def part1(puzzle_input: list) -> int:
    graph = _build_graph(puzzle_input)
    return _calculate_lowest_risk_level(graph)


def part2(puzzle_input: list) -> int:
    tile = _build_graph(puzzle_input)
    graph = _repeat_tile(tile, scale=5)
    return _calculate_lowest_risk_level(graph)


def _build_graph(puzzle_input: list) -> dict:
    graph = {}

    for y, line in enumerate(puzzle_input):
        for x, risk in enumerate(line):
            graph[(x, y)] = int(risk)

    return graph


def _repeat_tile(tile: dict, scale: int) -> dict:
    tile_dimension = math.sqrt(len(tile))
    graph = {}

    for (x, y), risk in tile.items():
        for x_offset in range(scale):
            for y_offset in range(scale):
                x2 = x + (x_offset * tile_dimension)
                y2 = y + (y_offset * tile_dimension)
                graph[(x2, y2)] = _wrap_number(risk + x_offset + y_offset)

    return graph


def _calculate_lowest_risk_level(graph: dict) -> int:
    dimension = math.sqrt(len(graph))
    goal = (dimension - 1, dimension - 1)
    start = (0, 0)
    
    path = _a_star(graph, start, goal)
    return functools.reduce(lambda acc, step: acc + graph[step], path, 0) - graph[start]


# Reference:
#   https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
#   https://www.redblobgames.com/pathfinding/a-star/implementation.html#optimize-queue
def _a_star(graph: dict, start: tuple, goal: tuple) -> list:
    priority_queue = []
    heapq.heappush(priority_queue, (_heuristic(start, goal), start))

    came_from = {}
    g_score = {start: 0}

    while len(priority_queue) > 0:
        current = heapq.heappop(priority_queue)[1]

        if current == goal:
            return _reconstruct_path(came_from, current)

        for neighbour in _get_neighbours(current):

            if neighbour not in graph:
                continue

            weight = graph[neighbour]
            tentative_g_score = g_score.get(current, math.inf) + weight

            if tentative_g_score < g_score.get(neighbour, math.inf):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score = tentative_g_score + _heuristic(neighbour, goal)
                heapq.heappush(priority_queue, (f_score, neighbour))


def _heuristic(node: tuple, goal: tuple) -> int:
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def _reconstruct_path(came_from: dict, current: tuple) -> list:
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def _get_neighbours(node: tuple) -> list:
    x, y = node
    return [(x, y + 1), (x - 1, y), (x + 1, y), (x, y - 1)]


def _wrap_number(n: int, lower: int = 1, upper: int = 9) -> int:
    return (n - lower) % (upper - lower + 1) + lower


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
