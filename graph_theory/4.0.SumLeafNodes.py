from queue import SimpleQueue


class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []


class Tree:
    def __init__(self, root=None):
        self.root = root


def build_tree():
    node1 = Node()
    node1.val = 2
    node2 = Node()
    node2.val = 9
    node3 = Node()
    node3.val = 1
    node3.children = [node1, node2]
    node4 = Node()
    node4.val = -6
    node5 = Node()dfs
    node5.val = 4
    node5.children = [node4, node3]

    node6 = Node()
    node6.val = 8
    node7 = Node()
    node7.val = 7
    node7.children = [node6]
    node8, node9 = Node(), Node()
    node8.val, node9.val = 0, -4
    node10 = Node()
    node10.val = 3
    node10.children = [node7, node8, node9]
    node11 = Node()
    node11.val = 5
    node11.children = [node5, node10]
    return node11


def print_bfs(node: Node) -> None:
    q = SimpleQueue()
    q.put(node)
    while not q.empty():
        n = q.get()
        global leaf_sum
        print(n.val)
        for k in n.children:
            q.put(k)


def sum_leaf_nodes(tree):
    """ """
    leaf_sum = 0

    def dfs(node: Node) -> None:
        """ """
        nonlocal leaf_sum
        if len(node.children) == 0:
            leaf_sum += node.val
        else:
            for n in node.children:
                dfs(n)

    dfs(tree)

    return leaf_sum


if __name__ == "__main__":
    tree = build_tree()
    print(sum_leaf_nodes(tree))
