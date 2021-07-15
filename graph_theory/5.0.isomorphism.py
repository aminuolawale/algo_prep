from typing import List
from queue import SimpleQueue as Queue


def isomorphic(g1: List[List[int]], g2: List[List[int]]) -> bool:
    t1, c1 = root_graph(g1)
    t2, c2 = root_graph(g2)
    e1 = ahu_encoding(c1, t1)
    e2 = ahu_encoding(c2, t2)
    print(e1, e2)
    return e1 == e2


def ahu_encoding(node, t: List[List[int]]) -> str:
    if len(t[node]) == 0:
        return "()"
    return f'({"".join(sorted([ahu_encoding(a,t) for a in t[node]], key=lambda a: -len(a)))})'


def root_graph(g: List[List[int]]) -> List[List[int]]:
    q = Queue()
    center = tree_center(g)[0]
    visited = [False for _ in g]
    rooted_graph = [[] for _ in g]
    q.put(center)
    visited[center] = True
    while not q.empty():
        node = q.get()
        children = g[node]
        for child in children:
            if not visited[child]:
                rooted_graph[node].append(child)
                q.put(child)
                visited[child] = True
    return rooted_graph, center


def tree_center(g: List[List[int]]) -> List[int]:
    degrees = [0 for _ in g]
    leaves = []
    for node, neighbors in enumerate(g):
        if len(neighbors) == 1:
            leaves.append(node)
        else:
            degrees[node] = len(neighbors)
    processed_nodes = len(leaves)
    while processed_nodes < len(g):
        new_leaves = []
        for leaf in leaves:
            neighbors = g[leaf]
            for n in neighbors:
                degrees[n] -= 1
                if degrees[n] == 1:
                    new_leaves.append(n)
            degrees[leaf] = 0
        processed_nodes += len(new_leaves)
        leaves = new_leaves
    return new_leaves


if __name__ == "__main__":
    g1 = [[1], [0, 2], [1], [4, 5], [1, 3], [3]]
    g2 = [[1], [0, 2], [1, 4], [4], [2, 3, 5], [4]]

    print(isomorphic(g1, g2))
