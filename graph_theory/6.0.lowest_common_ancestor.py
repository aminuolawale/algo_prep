from typing import List
from queue import SimpleQueue


def lca(a, b, a_list):
    """ """
    visited = [False for _ in a_list]
    prev = [None for _ in a_list]
    start = 0

    def breadth_first_search(start: int) -> List[int]:
        q = SimpleQueue()
        q.put(start)
        visited[start] = True
        while not q.empty():
            v = q.get()
            neighbors = a_list[v]
            for n in neighbors:
                if not visited[n]:
                    q.put(n)
                    visited[n] = True
                    prev[n] = v
        return prev

    ancestors = breadth_first_search(start)
    print(ancestors)
    a_path = build_path(start, a, ancestors)
    b_path = build_path(start, b, ancestors)
    print(a_path, b_path)
    k = set(a_path).intersection(set(b_path))
    k = list(k)
    return max(k)


def build_path(start: int, end: int, ancestor_array: List[int]) -> List[int]:
    iterator = end
    path = []
    while iterator is not None:
        path.append(iterator)
        iterator = ancestor_array[iterator]
    path = list(reversed(path))
    return path


if __name__ == "__main__":
    graph = [[1, 2], [], [3, 4], [5], [], []]
    print(lca(5, 5, graph))
