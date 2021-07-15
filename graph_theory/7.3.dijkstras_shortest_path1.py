from typing import List, Tuple
from queue import SimpleQueue as Q
import heapq

#How much improvement does using a priority queue provide?
# A little but not very much. We still end up with duplicate values in our queue but this time around we always encounter the shortest edge to any node first before
# the other  edges meaning that for any node, we update its distance significantly less frequently than when using a  normal queue
# In the case of a dense graph, this is not a significant improvement


def dijkstra(graph: List[List[Tuple[int, int]]]):
    distances = [float("inf") for _ in graph]
    ancestors = [None for _ in graph]
    q = []
    heapq.heappush(q, (0,0))
    while q:
        distance, node = heapq.heappop(q)
        print(node, distance)
        distances[node] = distance
        edges = graph[node]
        for edge in edges:
            child, child_distance = edge
            full_distance = distance + child_distance
            if full_distance < distances[child]:
                heapq.heappush(q,(full_distance, child))
                distances[child] = full_distance
                ancestors[child]= node
    return distances, ancestors

def shortest_path(start, end, graph)->List[int]:
    distances, ancestors = dijkstra(graph)
    iterator = end
    path = [iterator]
    while iterator != start:
        ancestor = ancestors[iterator]
        path.append(ancestor)
        iterator = ancestor
    return list(reversed(path))


heapq.heapreplace()
if __name__ == "__main__":
    graph = [[(2, 1), (1, 2)], [(2, 3), (3, 1)], [(4, 1), (3, 1)], [(4, 4)], []]
    graph = [
        [(1, 4), (2, 1)],
        [(3, 1)],
        [(1, 2), (3, 5)],
        [(4, 3)],[]
    ]
    print(shortest_path(0,4,graph))