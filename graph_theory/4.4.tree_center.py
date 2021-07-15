from typing import List
from graph_generator import GraphGenerator


def tree_center(adj_list: List[int]) -> int:
    tree_size = len(adj_list)
    degree = [0 for _ in range(tree_size)]
    leaves = []
    for i in range(tree_size):
        degree[i] = len(adj_list[i])
        if degree[i] in [0, 1]:
            leaves.append(i)
            degree[i] = 0
    count = len(leaves)
    while count < tree_size:
        new_leaves = []
        for node in leaves:
            for neighbor in adj_list[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
            degree[node] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


if __name__ == "__main__":
    adj_list = GraphGenerator()
    print(adj_list.render_list())
    print(tree_center(adj_list.render_list()))