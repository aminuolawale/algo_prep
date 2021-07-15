# undirected graphs
#     eulerian path:
#           at most two nodes have odd degrees while the rest even
#     eulerian circuit:
#           all nodes have even degrees


# directed graphs:
#       eulerian path:
#           at most one node has indeg- outdeg =1
#            atmost one node has outdeg - indeg = 1
#     eulerian circuit:
#              all nodes have indeg = outdeg
from typing import List, Tuple, Union


def eulerian_path(edges, n) -> List[List[int]]:
    in_array, out_array = process_graph(edges, n)
    if not in_array and out_array:
        print("edges has no eulerian path")
        return None
    start = get_starting_node(in_array, out_array)
    path = []
    visited = {}
    graph = edge_list_to_adjacency_list(edges, n)

    def dfs(node):
        nonlocal edges
        nonlocal visited
        nonlocal path
        nonlocal graph
        visited[node] = visited.get(node) or set()
        children = graph[node]
        for child in children:
            if not child in visited[node]:
                visited[node].add(child)
                dfs(child)
        path.append(node)

    dfs(start)
    return path[::-1]


def process_graph(edges, n) -> Union[Tuple[List[int], List[int]], bool]:
    in_array = [0 for _ in range(n)]
    out_array = [0 for _ in range(n)]
    for a, b in edges:
        out_array[a] += 1
        in_array[b] += 1
    overshoot = False
    undershoot = False
    for a, b in zip(in_array, out_array):
        if b - a > 1:
            return None, None
        if a - b > 1:
            return None, None
        if b - a == 1:
            if overshoot:
                return False
            overshoot = True
        if a - b == 1:
            if undershoot:
                return False
            undershoot = True
    return in_array, out_array


def get_starting_node(in_array, out_array) -> int:
    for i, a, b in zip(range(len(in_array)), in_array, out_array):
        if b - a == 1:
            return i
    for i, a in out_array:
        if a > 0 and b - a == 0:
            return i


def edge_list_to_adjacency_list(edges: List[List[int]], n: int) -> List[List[int]]:
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
    return graph


if __name__ == "__main__":
    edges = [
        (1, 2),
        (1, 3),
        (2, 2),
        (2, 4),
        (2, 4),
        (3, 1),
        (3, 2),
        (3, 5),
        (4, 3),
        (4, 6),
        (5, 6),
        (6, 3),
    ]
    print(eulerian_path(edges, 7))
