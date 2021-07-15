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


if __name__ == "__main__":
    graph = [
        [2, 3],
        [3, 4, 5],
        [4, 6],
        [6, 8],
        [8, 9],
        [7, 13, 14],
        [8, 12, 13],
        [9, 12],
        [10, 11],
        [11],
        [12, 15],
        [11, 15],
        [12],
        [15],
        [],
    ]

    visited = [False for _ in range(len(graph))]
    prev = [None for _ in range(len(graph))]
    print(shortest_path(2, 13))
