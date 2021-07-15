from typing import List
from algo_utils import print_bfs, Node
from queue import SimpleQueue as Q

# rooting an undirected tree


def root_tree(adj_list: List[int], designated_root: int) -> int:
    q = Q()
    node = Node(val=designated_root)
    q.put(node)
    visited = [False for _ in range(len(adj_list))]
    visited[node.val] = True
    while not q.empty():
        n = q.get()
        neighbors = adj_list[n.val]
        children = []
        for nay in neighbors:
            if not visited[nay]:
                child = Node(nay)
                q.put(child)
                visited[nay] = True
                children.append(child)
        n.children = children
    return node


if __name__ == "__main__":
    adj_list = [[1], [0, 2, 5, 4], [1, 3], [2], [1], [1, 6, 7], [5], [5, 8], [7]]
    root_node = root_tree(adj_list, 5)
    print_bfs(root_node)