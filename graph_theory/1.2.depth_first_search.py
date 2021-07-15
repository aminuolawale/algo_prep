from .algo_utils import count_vertices

graph = [[2, 3, 4], [4, 5], [6], [3, 5], [6], []]


visited = [False for _ in range(count_vertices(graph))]


def depth_first_search(start):
    if visited[start - 1]:
        return
    print(start)
    visited[start - 1] = True
    for n in graph[start - 1]:
        depth_first_search(n)


depth_first_search(1)
