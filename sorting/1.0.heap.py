from typing import List, Union
from queue import SimpleQueue as Q


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def heapify(arr: List[int]) -> List[int]:
    q = Q()
    index = 0
    q.put((None, Node(arr[index])))
    root = None
    while not q.empty():
        parent, node = q.get()
        if not root:
            root = node
        if parent:
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
        index += 1
        if index < len(arr):
            left = Node(arr[index])
            q.put((node, left))
        index += 1
        if index < len(arr):
            right = Node(arr[index])
            q.put((node, right))
    root = sort_heap(root)
    return root


def get_leaf(node:Node, depth = 0)->Node:
    if node is None:
        return None, depth
    a, b = get_leaf(node.left, depth + 1)
    c, d = get_leaf(node.right, depth + 1)
    if not a and not c:
        return node, depth
    if a and  b > d:
        return a, b
    return c, d


def heap_sort(arr:List[int])->List[int]:
    res = []
    heap = heapify(arr)
    heap_array = tree_to_array(heap)
    while len(res) < len(arr):
        res.append(heap.val)
        leaf, d  = get_leaf(heap)
        print(leaf, d)
        heap.val = leaf.val
        leaf = None
        heap = sort_heap(heap)
    return res


def sort_heap(node: Node) -> Node:
    if not node:
        return None
    left = sort_heap(node.left)
    right = sort_heap(node.right)
    if left and left.val > node.val:
        node.val, left.val = left.val, node.val
        sort_heap(node.left)
    if right and right.val > node.val:
        node.val, right.val = right.val, node.val
        sort_heap(node.right)
    return node


def tree_to_array(node: Node) -> List[int]:
    q = Q()
    q.put(node)
    out = []
    while not q.empty():
        n = q.get()
        out.append(n.val)
        if n.left:
            q.put(n.left)
        if n.right:
            q.put(n.right)
    return out


if __name__ == "__main__":
    arr = [15, 20, 7, 9, 30]
    heap = heapify(arr)
    print(tree_to_array(heap))
    print(heap_sort(arr))