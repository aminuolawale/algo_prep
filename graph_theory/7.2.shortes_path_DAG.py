from typing import List

# naturally I should do a top sort
def single_source_shortest_path(graph: List[List[int]]) -> List[int]:
    distances = [float("inf") for _ in graph]
    distances[0] = 0
    for node, children in enumerate(graph):
        for child, weight in children:
            new_dist = weight + distances[node]
            if new_dist < distances[child]:
                distances[child] = new_dist
    return distances



if __name__ == "__main__":
    graph = [
        [(1, 3), (2, 6)],
        [(3, 4), (4, 4), (5, 11)],
        [(3, 8), (6, 11)],
        [(4, -4), (5, 5), (6, 2)],
        [(7, 9)],
        [(7, 1)],
        [(7, 2)],
        [],
    ]
    ans = single_source_shortest_path(graph)
    print(ans) 