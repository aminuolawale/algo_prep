from random import choice


class Node:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


def root_tree(node):
    """ """
    return


def tree_centre(node):
    """ """

    def dfs(node, parent):
        print(node.val, parent.val)
        if len(node.children) == 1:
            print("-----------", node.val, parent.val)
            parent.children.remove(node)
            return parent
        else:
            for k in [a for a in node.children if a is not None]:
                return dfs(k, node)

    while len([a for a in node.children if a is not None]) >= 1:
        print([a.val for a in node.children])
        node = dfs(node, choice([a for a in node.children if a is not None]))
        print(node.val)
    return node


def undirected_tree():
    node2 = Node(2)
    node3 = Node(3)
    node2.children = [node3]
    node1 = Node(1)
    node6 = Node(6)
    node7 = Node(7)
    node7.children = [node3]
    node3.children = [node1, node7, node6, node2]
    node9 = Node(9)
    node6.children = [node9, node3]
    node9.children = [node6]
    node4 = Node(4)
    node0 = Node()
    node0.children = [node1]
    node1.children = [node4, node0, node3]
    node5 = Node(5)
    node5.children = [node4]
    node8 = Node(8)
    node8.children = [node4]
    node4.children = [node5, node8, node1]
    return node0


if __name__ == "__main__":
    tree = undirected_tree()
    node = tree_centre(tree)
    print(node.val)