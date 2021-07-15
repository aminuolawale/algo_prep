from algo_utils import Queue, count_vertices

graph = [[2, 3, 4], [4, 5], [6], [3, 5], [6], [7], []]
graphc = count_vertices(graph)


def bfs(start):
    q = Queue()
    prev = [None for _ in range(graphc)]
    visited = [False for _ in range(graphc)]
    print(start)
    q.enqueue(start)
    visited[start - 1] = True
    while not q.is_empty():
        node = q.dequeue()
        neighbors = graph[node - 1]
        for n in neighbors:
            if not visited[n - 1]:
                q.enqueue(n)
                print(n)
                visited[n - 1] = True
                prev[n - 1] = node
    return prev


def do(start):
    prev = bfs(start)
    return build_path(start, 7, prev)


def build_path(s, e, prev):
    path = []
    start = e
    while start is not None:
        path.append(start)
        start = prev[start - 1]

    path = [a for a in reversed(path)]
    print(path)

    return path


print(do(1))