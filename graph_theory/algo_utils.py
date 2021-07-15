from queue import SimpleQueue
import heapq


def count_vertices(graph):
    result = []
    for a in graph:
        result.extend(a)
    return len(set(result)) + 1


class PriorityQueue:
    def __init__(self):
        self.q = []
        heapq.heapify(self.q)

    def pull(self):
        return heapq.heappop(self.q)

    def insert(self, key, value):
        heapq.heappush(self.q, (key, value))

    def empty(self):
        return len(self.q) == 0


class Node:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


class BinaryNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.contents = [None for _ in range(capacity)]
        self.first = 0
        self.last = -1

    def is_empty(self):
        return self.last == -1 or all(a is None for a in self.contents)

    def enqueue(self, val):
        if self.last == len(self.contents) - 1:
            new_contents = [a for a in self.contents if a is not None]
            if len(new_contents) == len(self.contents):
                new_contents.extend([None for _ in range(len(new_contents))])
                self.contents = new_contents
        self.contents[self.last + 1] = val
        self.last += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception(message="Queue is empty")
        val = self.contents[self.first]
        self.contents[self.first] = None
        self.first += 1
        return val

    def print(self):
        for val in self.contents[self.first : self.last + 1]:
            print(val, end=", ")
        print()


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
    node5 = Node()
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


def print_bfs(node) -> None:
    q = SimpleQueue()
    q.put(node)
    while not q.empty():
        n = q.get()
        if not n:
            break
        global leaf_sum
        print(n.val if n else "")
        if hasattr(n, "children"):
            for k in n.children:
                q.put(k)
        elif hasattr(n, "left") or hasattr(n, "right"):
            if n.left:
                q.put(n.left)
            if n.right:
                q.put(n.right)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(55)
    q.enqueue(56)
    q.enqueue(67)
    q.enqueue(78)
    q.enqueue(123)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)
    q.enqueue(1122)

    q.print()
    a = q.dequeue()
    print("---------------", a)
    q.print()
