from typing import List
from queue import LifoQueue as Q
from random import choice

def tarjan(graph:List[List])->List[int]:
    def dfs(node):
        nonlocal graph
        nonlocal low_link_values
        nonlocal q
        nonlocal visited
        nonlocal on_stack
        q.put(node)
        on_stack[node] = True
        visited.add(node)
        children = graph[node]
        low_link = node
        for child in children:
            if child not in visited:
                q.put(child)
                on_stack[child] = True
                new_low_link = dfs(child)
                print("^^^^^^^^^^^^^^^", new_low_link)
                if on_stack[child]:
                    print("%%%%%%%%%%%%%%%%%%%%")
                    low_link = min(low_link, new_low_link)

        if low_link == node:
            print(">>>>>>>>>>>>>", node)
            while True:
                val = q.get()
                on_stack[val] = False
                print("--", val, "--")
                if val == node:
                    break
        low_link_values[node] = low_link
        return low_link
    q = Q()
    low_link_values = [None for _ in graph]
    on_stack = [False for _ in graph] 
    visited = set()
    node = 0
    low_link_values[node] = node
    while True:
        ll = dfs(node)
        print(ll, "!!!!!!!!1")
        print(visited)
        if len(visited) == len(graph):
            break
        node = choice([a for a in range(len(graph)) if a not in visited])
        print(node, "/////////////////")
    return low_link_values
    
def peek(q):
    val= q.get()
    q.put(val)
    return val


if __name__ =="__main__":
    graph = [
        [1],
        [2],
        [0],
        [4,7],
        [5],
        [0,6],
        [0,2],
        [3,5]
    ]
    print(tarjan(graph))