from typing import List
from queue import SimpleQueue


def shortest_path(start: int, end: int) -> List[int]:
    ancestor_array = breadth_first_search(start)
    return build_path(start, end, ancestor_array)


def build_path(start: int, end: int, ancestor_array: List[int]) -> List[int]:
    iterator = end
    path = []
    while iterator is not None:
        path.append(iterator)
        iterator = ancestor_array[iterator - 1]
    path = list(reversed(path))
    return path


def breadth_first_search(start: int) -> List[int]:
    q = SimpleQueue()
    q.put(start)
    visited[start - 1] = True
    while not q.empty():
        v = q.get()
        neighbors = graph[v - 1]
        for n in neighbors:
            if not visited[n - 1]:
                q.put(n)
                visited[n - 1] = True
                prev[n - 1] = v
    return prev


def grid_to_adjacency_list(grid: List[List[int]]) -> List[List[int]]:
    # north, south, west, east
    vertical_offset = [1, -1, 0, 0]
    horizontal_offset = [0, 0, -1, 1]
    adjacency_list = []
    for row_index, row in enumerate(grid):
        for element_index, element in enumerate(row): 
            entry = []
            if element != 1:
                for i in range(len(vertical_offset)):
                    x = element_index + horizontal_offset[i]
                    y = row_index + vertical_offset[i]
                    if x < 0 or x >= len(row):
                        continue
                    if y < 0 or y >= len(grid):
                        continue
                    if grid[y][x] != 1:
                        entry.append(x + 1 + y * len(row))
            adjacency_list.append(entry)

    return adjacency_list


if __name__ == "__main__":
    from pprint import pprint

    dungeon = [
        [0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0],
    ]
    graph = grid_to_adjacency_list(dungeon)
    prev = [None for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    start = 1
    end = 35
    print(shortest_path(start, end))
