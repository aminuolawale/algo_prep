from typing import Any, List
"""

How would a network graph be represented?
As a list of edges. Each edge will contain extra information about the edge capacity and flow
[from, to, capacity, flow]
"""
network = [
    [0, 1, 10, 0],
    [0, 2, 10, 0],
    [1, 3, 25, 0],
    [2, 4, 15, 0],
    [4, 1, 6, 0],
    [4, 5,10, 0],
    [3, 5, 10, 0]
]



""" 
Finding an augmenting path.
Do dfs till we get to the sink making sure to take only unsaturated edges.
"""
Graph = List[List[int]]
def edge_list_to_adjacency_list(edges:Graph)-> Graph:
    """ """
    store = {}
    for edge in edges:
        a, b = edge[0:2]
        if a not in store:
            store[a] = []
        store[a].append([b, edge[2], edge[3]])
    node_count = len(store) + 1
    adjacency_list = [[] for _ in range(node_count)]
    for node, neighbors in store.items():
        adjacency_list[node] = neighbors
    return adjacency_list

def find_augmenting_path(graph:Graph) -> Graph:
    """ """
    graph = edge_list_to_adjacency_list(graph)
    source_node = 0
    augmenting_path, bottleneck_value, graph = depth_first_search(source_node, graph)
    return augmenting_path[::-1], bottleneck_value, graph


def depth_first_search(node:int, graph:Graph, bottleneck:int=float("inf"))-> List[int]:
    """ """    
    neighbors= graph[node]
    for index,neighbor_data in enumerate(neighbors):
        if is_unsaturated(neighbor_data):
            bottleneck = min(neighbor_data[-2], bottleneck)
            neighbor_node = neighbor_data[0]
            path_section, bottleneck, graph= depth_first_search(neighbor_node, graph, bottleneck)
            neighbor_data[-1] = bottleneck
            neighbors[index] = neighbor_data
            graph[node] = neighbors
            path_section.append(node)
            remaining_capacity = neighbor_data[1] - neighbor_data[2]
            return path_section, bottleneck, graph
    return [node], bottleneck, graph
    
def is_unsaturated(node_data)-> bool:
    return node_data[-1] < node_data[-2]
    

if __name__ == "__main__":
    network = [
        [0, 1, 10, 10],
    [0, 2, 10, 0],
    [1, 3, 25, 0],
    [2, 4, 15, 0],
    [4, 1, 6, 0],
    [4, 5,10, 0],
    [3, 5, 10, 0]]
    print(network)
    a, b, c = find_augmenting_path(network)
    print(a)
    print(b)
    print(c)