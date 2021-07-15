from typing import List, Tuple

def bellman_ford(graph:List[List[Tuple[int]]]):
    """ """
    distances = [float("inf") for _ in graph]
    distances[0]  = 0
    first_pass = None
    for _ in range(len(graph)-1):
        for node, children in enumerate(graph):
            for child, dist in children:
                distances[child] = min(dist + distances[node], distances[child])
    first_pass = [a for a in distances]
    for _ in range(len(graph)-1):
        for node, children in enumerate(graph):
            for child, dist in children:
                distances[child] = min(dist + distances[node], distances[child])
                if distances[child] < first_pass[child]:
                    distances[child] = float("-inf")
    return distances



if __name__ == "__main__":
    graph = [
        [(1,5)],
        [(2,20),(5,30),(6,60),],
        [(3,10),(4,75),],
        [(2,-15)],
        [(9,100),],
        [(4,25),(6,5),(8,50)],
        [(7,-50),],
        [(8,-10),],
        [],
        []
    ]
    print(bellman_ford(graph))