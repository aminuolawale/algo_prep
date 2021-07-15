from algo_utils import Queue, count_vertices

graph = [[2, 3, 4], [4, 5], [6], [3, 5], [6], []]


def bfs(start):
    print(start)
    q = Queue()
    q.enqueue(start)
    visited = [False for _ in range(count_vertices(graph))]
    visited[start - 1] = True
    prev = [None for _ in range(count_vertices(graph))]
    while not q.is_empty():
        node = q.dequeue()
        neighbors = graph[node - 1]
        for neigh in neighbors:
            if not visited[neigh - 1]:
                print(neigh)
                q.enqueue(neigh)
                visited[neigh - 1] = True
                prev[neigh - 1] = node
    return prev


print(bfs(1))