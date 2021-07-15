from typing import List, Dict

graph = {3: [2, 4], 2: [4, 11, 13], 4: [11], 11: [13], 13: [6]}
Graph = Dict[int, List[int]]
Visited = Dict[int, bool]


def depth_first_search(start: int, graph: Graph, visited: Visited) -> None:
    if visited.get(start):
        return
    print(start)
    visited[start] = True
    neighbours = graph.get(start)
    if not neighbours:
        return
    for neig in neighbours:
        depth_first_search(neig, graph, visited)


depth_first_search(3, graph, {})