from typing import List
import math

# refactor with last seen index


def eulerian_tour(tree: List[List[int]]):
    tour = []
    depth = []

    def dfs(node: int, d=0) -> None:
        nonlocal tree
        nonlocal tour
        tour.append(node)
        depth.append(d)
        children = tree[node]
        for child in children:
            dfs(child, d + 1)
            tour.append(node)
            depth.append(d)

    dfs(0)
    return tour, depth


def lca(tree: List[List[int]], a: int, b: int) -> int:
    tour, depth = eulerian_tour(tree)
    aindex = tour.index(a)
    bindex = tour.index(b)
    first = min(aindex, bindex)
    second = max(aindex, bindex)
    rmq = float("inf")
    rmq_index = None
    for i, a in enumerate(depth[first : second + 1]):
        if rmq > a:
            rmq_index = i
            rmq = a
    return tour[rmq_index + first]


if __name__ == "__main__":
    graph = [[1, 2], [3], [4, 5], [], [6], [], []]
    print(lca(graph, 1, 5))
