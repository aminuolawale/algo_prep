from string import ascii_lowercase


class Edge:
    def __init__(self, a, b, w):
        self.nodes = [a, b]
        self.w = w

    def __eq__(self, x):
        return set(self.nodes) == set(x.nodes) and self.w == x.w

    def __hash__(self):
        return max(self.nodes) + min(self.nodes) + self.w
    def nodes_list(self):
        return self.nodes

    def __repr__(self):
        return f"{(*self.nodes_list(), self.w)}"


def kruskal(node, graph, visited, tree):
    children = graph[node]
    minimum_weight = float("inf")
    minimum_node = None
    for child in children:
        if not visited[child]:
            weight = self.kruskal(child, graph, visited, tree)
            if weight < minimum_weight:
                minimum_weight = weight
                minimum_node = child


def min_span_tree(graph):
    graph = sorted(graph, key = lambda a: a[-1])
    edges = sorted(get_edges(graph), key =lambda a : a.w)
    unified = {}
    tree = [[] for _ in graph]
    for edge in edges:
        if not unified.get(edge):
            nodes_list = edge.nodes_list()
            tree[nodes_list[0]].append((nodes_list[1], edge.w))
            tree[nodes_list[1]].append((nodes_list[0], edge.w))
            unified[edge] = True
    print(unified)
    print(len(unified))
    return tree





def build_adjacency_list(map_graph):
    global ascii_lowercase
    ascii_lowercase = ascii_lowercase[:10]
    result = [[] for _ in map_graph]
    for index, letter in enumerate(ascii_lowercase):
        raw = map_graph[letter]
        raw = [(ascii_lowercase.index(a[0]), a[1]) for a in raw]
        result[index] = raw
    return result


def get_edges(graph):
    edges = set()
    for node, children in enumerate(graph):
        childs = graph[node]
        for c, w in childs:
            edge = Edge(node, c, w)
            edges.add(edge)
    return list(edges)


if __name__ == "__main__":
    raw_graph = {
        "a": [
            ("b", 5),
            ("d", 9),
            ("e", 1),
        ],
        "b": [
            ("a", 5),
            ("c", 4),
            ("d", 2),
        ],
        "c": [("b", 4), ("h", 4), ("i", 1), ("j", 8)],
        "d": [("a", 9), ("b", 2), ("e", 2), ("f", 5), ("g", 11), ("h", 2)],
        "e": [("a", 1), ("d", 2), ("f", 1)],
        "f": [
            ("e", 1),
            ("g", 7),
            ("d", 5),
        ],
        "g": [("f", 7), ("d", 11), ("h", 1), ("i", 4)],
        "h": [
            ("d", 2),
            ("g", 1),
            ("i", 6),
            ("c", 4),
        ],
        "i": [("g", 4), ("h", 6), ("c", 1), ("j", 0)],
        "j": [("i", 0), ("c", 8)],
    }
    graph = build_adjacency_list(raw_graph)
    print(min_span_tree(graph))