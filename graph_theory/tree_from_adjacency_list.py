from typing import List, Any
from queue import SimpleQueue


class Node:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


def tree_from_adjacency_list(adj_list: List[List[Any]]) -> Node:
    """ """
    q = SimpleQueue()
    index = 0
    root_value = index
    root = Node(root_value)
    q.put(root)
    while not q.empty():
        node = q.get()
        node.children = []
        for child_value in adj_list[node.val]:
            child_node = Node(child_value)
            node.children.append(child_node)
            q.put(child_node)
    return root


def print_bfs(node: Node):
    q = SimpleQueue()
    q.put(node)
    while not q.empty():
        n = q.get()
        print(n.val)
        for c in n.children:
            q.put(c)


def encode_tree(node: Node):
    if len(node.children) == 0:
        return "()"
    encoding = sorted([encode_tree(a) for a in node.children], key=lambda a: -len(a))
    return f"({''.join(encoding)})"


if __name__ == "__main__":
    adj_list = [[2, 1, 3], [4, 5], [6, 7], [8], [], [9], [], [], [], []]
    adj_list2 = [[1, 2, 3], [], [], [4, 5], [6, 7], [9], [], [8], [], []]
    tree = tree_from_adjacency_list(adj_list)
    tree2 = tree_from_adjacency_list(adj_list2)
    # I need to center both trees.a
    print_bfs(tree2)
    tree_encoding = encode_tree(tree)
    tree_encoding2 = encode_tree(tree2)
    print(tree_encoding, tree_encoding2)
