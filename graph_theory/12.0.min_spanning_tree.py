from queue import SimpleQueue as Q
from typing import List, Tuple
import heapq
from algo_utils import PriorityQueue

# this implementation works but the real algorithm uses a priority queue
#  why is a priority queue better in this algorithm?


def min_spanning_tree(
    graph: List[List[(Tuple[int, int])]], n:int
) -> List[List[Tuple[int, int]]]:
    node = 0
    visited = set()
    q = PriorityQueue()
    raw_tree = []
    cost = 0
    seen_with = [float("inf") for _ in range(n)]
    while len(raw_tree) < n:
        edges = get_edges(node, graph)
        for edge in edges:
            if edge[1] not in visited:
                q.insert(edge[-1], edge[:2])
        visited.add(node)
        if q.empty():
            break
        w, (par, node) = q.pull()
        while node in visited and not q.empty():
            w, (par, node) = q.pull()
        if seen_with[node] > w:
            raw_tree.append((par, node, w))
            seen_with[node] = w
    cost = sum(a[-1] for a in raw_tree)
    tree_center, tree = find_tree_center(raw_tree, n)
    tree = root_tree(tree, tree_center)
    return tree, cost

def get_edges(node, edges):
    start = 0
    end = len(edges)
    res = []
    while start < end:
        mid = (start + end)//2
        val = edges[mid][0]
        if val < node:
            start = mid + 1
        elif val > node:
            end = mid - 1
        else:
            res.append(edges[mid])
            a = mid - 1
            b = mid + 1
            while  (a > -1 or b < len(edges)) :
                if a > -1 and edges[a][0] == node:
                    res.append(edges[a])
                if b < len(edges) and  edges[b][0] ==node:
                    res.append(edges[b])
                a -= 1
                b += 1
            
            return res


def root_tree(
    tree: List[List[Tuple[int, int]]], node: int
) -> List[List[Tuple[int, int]]]:
    visited = [False for _ in tree]
    res = [[] for _ in tree]
    q = Q()
    q.put(node)
    visited[node] = True
    while not q.empty():
        node = q.get()
        children = tree[node]
        for child, weight in children:
            if not visited[child]:
                visited[child] = True
                q.put(child)
                res[node].append((child, weight))

    return res



def edges_to_adj_list(edges, n):
    out = [[] for _ in range(n)]
    for f,t,w in edges:
        out[f].append((t,w))
        out[t].append((f,w))
    return out



def find_tree_center(tree, n) -> int:
    tree = edges_to_adj_list(tree, n)
    degs = [0 for _ in tree]
    leaves = []
    for node, children in enumerate(tree):
        degs[node] = len(children)
        if degs[node] <= 1:
            leaves.append(node)
    processed = len(leaves)
    while processed < len(tree):
        new_leaves = []
        for node in leaves:
            degs[node] = 0
            for k, weight in tree[node]:
                degs[k] -= 1
                if degs[k] <= 1:
                    new_leaves.append(k)
        leaves = new_leaves
        processed += len(leaves)
    return leaves[0], tree


if __name__ == "__main__":

    edges = [
        (0, 1, 10),
        (0, 2, 1),
        (0, 3, 4),
        (1, 0, 10),
        (1, 2, 3),
        (1, 4, 0),
        (2, 0, 1),
        (2, 1, 3),
        (2, 3, 2),
        (2, 5, 8),
        (3, 0, 4),
        (3, 2, 2),
        (3, 5, 2),
        (3, 6, 7),
        (4, 1, 0),
        (4, 5, 1),
        (4, 7, 8),
        (5, 4, 1),
        (5, 2, 8),
        (5, 7, 9),
        (5, 6, 6),
        (5, 3, 2),
        (6, 3, 7),
        (6, 5, 6),
        (6, 7, 12),
        (7, 4, 8),
        (7, 5, 9),
        (7, 6, 12),
    ]
    print(min_spanning_tree(edges, 8))
