from typing import List

def travelling_salesman(adj_matrix, start):
    size = len(adj_matrix) * len(adj_matrix[0])
    cache = [[float("inf") for _ in range(size)] for  _ in range(2**size)]
    cache = setup(adj_matrix, cache, start, size)
    cache = solve(adj_matrix, cache, start, size)
    min_cost = find_min_cost(adj_matrix, cache, start, size)
    tour =find_optimal_tour(adj_matrix, cache, start, size)
    return min_cost, tour



def setup(adj_matrix, cache, start, size)-> List[List[int]]:
    print(start, len(adj_matrix), size)
    for i in range(size):
        if i == start:
            continue
        cache[i][1 << start | 1 << i] = adj_matrix[start][i]    
    return cache

def solve(adj_matrix, cache, start, size):
    for r in range(3, size+1):
        for subset in bit_combinations(r, size):
            if not_in(start, subset):
                continue
            for next_node in range(size):
                if next_node == start or not_in(next, subset):
                    continue
                state = subset ^ (1 << next_node)
                min_distance = float("inf")
                for end_node in range(size):
                    if end_node == start or end_node == next_node or not_in(end_node, subset):
                        continue
                    new_distance = cache[end_node][state] + adj_matrix[end_node][next_node]
                    if new_distance < min_distance:
                        min_distance = new_distance
                    cache[next_node][subset] = min_distance 
    return cache

def not_in(i, subset):
    return ((1 << i) & subset) == 0

def find_min_cost(adj_matrix, cache, start, size):
    END_STATE = (1 << size) - 1
    min_tour_cost =float("inf")
    for end_node in range(size):
        if end_node == start:
            continue
        tour_cost = cache[end_node][END_STATE] + adj_matrix[end_node][start]
        min_tour_cost = min(min_tour_cost, tour_cost)
    return min_tour_cost

def find_optimal_tour(adj_matrix, cache, start, size):
    prev_index = start
    state = (1<<size) -1
    tour = [None for _ in range(size + 1)]
    for i in range(size-1, 0, -1):
        index = -1
        for j in range(size):
            if j == start or not_in(j, state):
                continue
            if index == -1 :
                index = j
            prev_distance = cache[index][state] + adj_matrix[j][prev_index]
            new_distance = cache[j][state] + adj_matrix[j][prev_index]
            if new_distance < prev_distance:
                index = j
        tour[i] = index
        state = state ^ (1<<index)
        prev_index = index
    tour[0] = tour[size] = start
    return tour



def bit_combinations(r, size, buff="", res=[])-> List[int]:
    if len(buff) == size:
        if r == 0:
            res.append(buff)
        return
    if r > 0:
        bit_combinations(r-1, size, buff+"1", res)
    if r >=0:
        bit_combinations(r, size, buff +"0", res)
    return [binary_to_decimal(a) for a in res]

def binary_to_decimal(a):
    res = 0
    for i, l in enumerate(a[::-1]):
        res += int(l) * 2 ** i
    return res

if __name__ == "__main__":
    matrix = [
        [0, 2, float("inf"), -1],
        [2, 0, 4, 6],
        [float("inf"), 4, 0, 3],
        [-1, 6, 3, 0],
    ]
    print(travelling_salesman(matrix,0))