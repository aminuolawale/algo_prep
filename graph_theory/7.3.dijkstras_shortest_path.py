# recalling the algorithm
# graph must be directed and acyclic
# no negative weights
# start at a node:
# enqueue the shortest paths to the neighboring nodes on a priority queue
# store the shortest distances in some array
# loop:
#   pop item from queue
#   update distance in distance array
#   enqueue children with their respective distances
# At the end we should have the distances array entirely populated with the shortest paths to each node
# why does this not work if there are negative weights?
#
# WARNING:
# This implementation does not use a priority queue. Because of this, previous nodes might be revisited after other nodes have been processed. 
# Also, we can't take advantage of the fact that we can stop once we have finished processing our destination node, due to the fact that our implementation
# makes it such that a node might be revisited in the future
# So, I should reimplement this with a priority queue
from typing import List, Tuple
from queue import SimpleQueue as Q


def dijkstra(graph: List[List[Tuple[int, int]]]):
    distances = [float("inf") for _ in graph]
    ancestors = [None for _ in graph]
    q = Q()
    q.put((0, 0))
    while not q.empty():
        node, distance = q.get()
        print(node, distance)
        distances[node] = distance
        edges = graph[node]
        for edge in edges:
            child, child_distance = edge
            full_distance = distance + child_distance
            if full_distance < distances[child]:
                q.put((child, full_distance))
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



if __name__ == "__main__":
    graph = [[(2, 1), (1, 2)], [(2, 3), (3, 1)], [(4, 1), (3, 1)], [(4, 4)], []]
    graph = [
        [(1, 4), (2, 1)],
        [(3, 1)],
        [(1, 2), (3, 5)],
        [(4, 3)],[]
    ]
    print(shortest_path(0,4,graph))