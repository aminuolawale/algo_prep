from algo_utils import build_tree, print_bfs
from typing import List
from queue import SimpleQueue


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def tree_height(node):
    if not any([node.left, node.right]):
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def build_tree_from_list(l: List) -> Node:
    """ """
    q = SimpleQueue()
    index = 0
    level = 0
    val = l[index]
    node = Node(val)
    q.put(node)
    k = index + 1
    while k < len(l):
        next_subarray = l[k : k + 2 ** (level + 1)]
        j = k
        print(next_subarray)
        while j < (k + (2 ** (level + 1))):
            n = q.get()
            left = Node(val=l[j])
            right = Node(val=l[j + 1])
            n.left = left
            n.right = right
            q.put(left)
            q.put(right)
            j += 2
        k = j
        level += 1
    return node


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, None, 9, 10]
    tree = build_tree_from_list(array)
    print(tree_height(tree))