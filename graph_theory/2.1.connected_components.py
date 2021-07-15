n = 8
graph = [[1, 3], [2], [3], [], [5, 6], [7], [5, 7], []]
count = 0
components = [None for _ in range(n)]
visited = [False for _ in range(n)]


def count_components():
    global count
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count, components


def dfs(start: int):
    visited[start] = True
    print(start)
    components[start] = count

    for _next in graph[start]:
        if not visited[_next]:
            dfs(_next)


print(count_components())