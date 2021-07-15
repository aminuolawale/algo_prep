graph = {1: [2, 9], 2: [13], 11: [4, 6], 13: [9], 6: [], 4: [6]}


def connected_components() -> int:
    count = 0
    no_of_visited = 0
    visited = {}
    x = list(graph.keys())
    y = []
    for j in graph.values():
        y.extend([*j])
    x = x + y
    p = set(x)
    for a in p:
        visited.update({a: False})
    start = list(graph.keys())[0]
    while no_of_visited < 8:
        no_of_visited, visited = dfs1(start, no_of_visited, visited)
        count += 1
        seen = None
        for k, v in visited.items():
            if not v and graph.get(k):
                start = k
                seen = True
        if not seen:
            break
    return count


def dfs1(start: int, n: int, visited) -> int:
    if visited.get(start):
        return n, visited
    visited.update({start: True})
    n += 1
    neighbours = graph.get(start)
    if neighbours is None or len(neighbours) == 0:
        return n, visited
    for neighbour in neighbours:
        return dfs1(neighbour, n, visited)


print(connected_components())