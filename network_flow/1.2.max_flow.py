from typing import List 

class Edge:
    def __init__(self, a:int, b:int, capacity:int, flow:int=0) -> None:
        self.a = a
        self.b = b
        self.capacity = capacity
        self.flow = flow
    
    def get_residual(self):
        return self(self.b, self.a, 0)

class Graph:
    def __init__(self, node_count) -> None:
        self.nodes = [[] for _ in range(node_count)]


    def add_edge(self, edge: Edge):
        residual_edge = edge.get_residual()
        a, b = edge.a, edge.b
        self.nodes[a].append(edge)
        self.nodes[b].append(residual_edge)

        
class FordFulkerson:
    def __init__(self, graph:Graph):
        self.graph = graph


    def solve(self):
        """ """
        start_node = 0

    def depth_first_search(self, start_node:int):







if __name__ == "__main__":
    edge_list = [
        [0, 1, 10],
        [0,2,5],
        [0,3,10],
        [1,4,10],
        [2,3,10],
        [3,6,15],
        [4,2,20],
        [5,2,15],
        [5,4,3],
        [6,5,4],
        [4,7,15],
        [7,8,10],
        [8,5,10],
        [8,6,7],
        [6,9, 10],
        [9,10,10],
        [7,10, 15]
    ]
    graph = Graph()
    for edge in edge_list:
        edge_object = Edge(*edge)
        graph.add_edge(edge_object)

