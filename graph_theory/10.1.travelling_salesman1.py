def travelling_salesman(adj_matrix, start):
    nodes = set()
    for node, _ in enumerate(adj_matrix):
        nodes.add(node)
    shortest = solve(0, adj_matrix, nodes, start)
    return shortest


def solve(node, adj_matrix, prevs, start, level=0):
    if not len(prevs):
        return adj_matrix[node][start]
    the_min = float("inf")
    min_node = None
    for c in prevs:
        val = adj_matrix[node][c] + solve(c, adj_matrix, prevs - {c}, start, level+ 1)
        if val < the_min:
            the_min = val
            min_node = c
    return the_min


if __name__ == "__main__":
    matrix =[[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    path = [None for _ in range(len(matrix)+1)]
    print(travelling_salesman(matrix, 0))