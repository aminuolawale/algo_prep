# The algorithm:
# Start at a node
# plunge depth first till a tail or a cycle while pushing all the encountered nodes onto a stack
# the low link value of the tail node is itself or the beginning of the cycle if it connects back to one
# we back track, and at each node we update its low link to the min of its lowlink and that of its child/children.
#   note that only children that have not been visited and that are currently on the stack are visited.
# Once we arrive at a node whose low link value remains itself, we are at the beginning of the strongly connected component
# we pop all the nodes in the component off the stack. and set them all to visited.
#  we represent our graph as an adjacency matrix

from queue import LifoQueue as Stack
from typing import List
from random import choice

def tarjan(graph:List[List[int]])-> List[int]:
    visited = set()
    low_links = [i for i, _ in enumerate(graph)]
    on_stack = [False for _ in graph]
    ids = [None for _ in graph]
    stack = Stack()
    def dfs(node:int) -> int:
        nonlocal graph
        nonlocal stack
        nonlocal on_stack
        stack.put(node)
        visited.add(node)
        on_stack[node] = True
        children = graph[node]
        low_links[node] = node
        for child in children:
            if not child in visited:
                dfs(child)
            if on_stack[child]:
                low_links[node] = min(low_links[node], low_links[child])
        if low_links[node] == node:
            while True:
                value = stack.get()
                on_stack[value] = False
                if value == node:
                    break
    node = 0
    while True:
        dfs(node)
        remainder = [i for i, _ in enumerate(graph) if not i in visited]
        if len(remainder) ==  0:
            break

        node = remainder[0]
    return low_links



if __name__ == "__main__":
    graph = [
        [1],
        [2],
        [0],
        [4,7],
        [5],
        [0,6],
        [0,2, 4],
        [3,5]
    ]
    print(tarjan(graph))