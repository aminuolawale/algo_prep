from typing import List, Tuple
from queue import SimpleQueue as Queue

# algorithm: build a list that maps to the number of nodes that point to a particular node


def build_degree_list(graph: List[List[int]]) -> Tuple[List[int], int]:
    degrees = [0 for _ in graph]
    for node, children in enumerate(graph):
        for child in children:
            degrees[child] += 1
    return degrees


def kahn(graph: List[List[int]]) -> List[int]:
    degrees= build_degree_list(graph)
    q = Queue()
    for i, d in enumerate(degrees):
        if d == 0:
            q.put(i)
    result = []
    while not q.empty():
        node = q.get()
        result.append(node)
        for child in graph[node]:
            degrees[child] -=1
            if degrees[child] == 0:
                q.put(child)
    if len(result) != len(graph):
        print("graph is cyclic")
        return None
    return result


if __name__ == "__main__":
    graph = [
        [2, 3,6], 
        [4], 
        [6], 
        [1,4], 
        [5,8], 
        [],
        [7,11],
        [4,12],
        [],
        [2,10],
        [6],
        [12],
        [8],
        []
        ]
    ans = kahn(graph)
    print(ans)