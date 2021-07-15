from typing import List


def tree_center(graph: List[List[int]]) -> List[int]:
    degrees = [0 for _ in range(len(graph))]
    leaves = []
    for index, node in enumerate(graph):
        if len(node) == 1:
            leaves.append(index)
        else:
            degrees[index] = len(node)
    print(leaves)
    count = len(leaves)
    while count < len(graph):
        new_leaves = []
        for leaf in leaves:
            neighbors = graph[leaf]
            degrees[leaf] = 0
            for n in neighbors:
                degrees[n] -= 1
                if degrees[n] == 1:
                    new_leaves.append(n)
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


if __name__ == "__main__":
    graph = [[1], [0, 3, 4], [3], [1, 2, 6, 7], [1, 5, 8], [4], [3, 9], [3], [4], [6]]
    print(tree_center(graph))
