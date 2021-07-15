from typing import List, Dict

graph = {3: [2, 4], 2: [4, 11, 13], 4: [11], 11: [13], 13: [6]}
visited = {}
Graph = Dict[int, List[int]]
Visited = Dict[int, bool]


def depth_first_search(start: int):
    if visited.get(start):
        return
    print(start)
    visited.update({start: True})
    neighbours = graph.get(start)
    if neighbours is None or len(neighbours) == 0:
        return
    for neighbour in neighbours:
        depth_first_search(neighbour)


depth_first_search(3)