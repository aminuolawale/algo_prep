from typing import List


def top_sort(g: List[List[int]]):
    visited = [False for _ in g]
    start_node = 4
    ordering = []

    def dfs(node: int) -> None:
        nonlocal visited
        nonlocal g
        visited[node] = True
        children = g[node]
        for child in children:
            if not visited[child]:
                dfs(child)
                ordering.append(child)

    dfs(start_node)
    ordering.append(start_node)
    return list(reversed(ordering))


if __name__ == "__main__":
    g = [[1, 2], [2, 3], [3, 4], [4, 7], [5, 6], [7], [], []]
    print(top_sort(g))
