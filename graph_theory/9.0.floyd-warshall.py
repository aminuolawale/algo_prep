from typing import List

def floyd_warshall(graph:List[List[int]])->List[List[int]]:
    size = len(graph)
    distances = [[a for a in b] for b in graph]
    next = [[-1 for a in b ] for b in graph]
    for i, r in enumerate(distances):
        for j, c in enumerate(r):
            if c < float("inf"):
                next[i][j] = j

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if  distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j] 
                    next[i][j] = next[i][k]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if  distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = float("inf")
                    next[i][j] = -1

    return distances, next



def shortest_path(start:int,end:int, graph:List[List[int]])->List[int]:
    distances, next = floyd_warshall(graph)
    if distances[start][end] == float("inf"):
        return None
    iterator = start
    path = [iterator]
    while iterator != end:
        iterator = next[iterator][end]
        if not iterator:
            return None
        path.append(iterator)
    return path




if __name__ == "__main__":
    graph = [
       [0, 1 , float("inf"), 2, float("inf"), -1, float("inf"),float("inf")],
       [float("inf"), 0, 3, 4, float("inf"), float("inf"), float("inf"), float("inf")],
       [float("inf"), float("inf"), float("inf"), float("inf"), -2, float("inf"), float("inf"),float("inf")],
       [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 4,3, float("inf")],
       [float("inf"), float("inf"),float("inf"), 1, float("inf"), float("inf"), float("inf"), float("inf")],
       [float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),],
       [float("inf"),float("inf"),float("inf"),float("inf"),float("inf"), -2, float("inf"), 0],
       [float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),-1, float("inf"), float("inf")]
    ]
    print(floyd_warshall(graph))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(shortest_path(1,5, graph))