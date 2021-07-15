from typing import List, Set, Tuple
import math

Polygon = Set[List[int]]
Coord = Tuple[int, int]
"""
This algorithm is wrong nonetheless. Only meant to illustrate the pitfalls of poor modelling.
"""


def closest_pair(points: List[Coord]) -> Polygon:
    """
    Algorithm:
    find and connect all closest vertices forming a chain.
    Then connect the last two vertices
    Outstanding:
    Connecting the last 2 vertices -> I am having issues doing this probably because of my decision to represent the polygon as a list of 
    edges instead of an adjacency list. 
    Bugs:
    Closest vertices not being connected in some cases. Much further apart vertices were being connected.
    e.g for the sample input in this code


    """
    edges = set()
    n = len(points)
    for _ in range(n-1):
        min_dist = float("inf")
        to_be_connected = None
        for j, point in enumerate(points):
            k = j + 1
            while k < len(points):
                pair = (point, points[k])
                if pair not in edges:
                    dist = euclidean_distance(pair)
                    if dist < min_dist:
                        to_be_connected = pair
                        min_dist = dist
                k += 1
        if to_be_connected not in edges:
            edges.add(to_be_connected)

    return edges


def terminal_vertices(edges: Polygon):
    index = 0
    while True:
        edge = edges[index]


def euclidean_distance(pair: Tuple[Coord, Coord]) -> float:
    a, b = pair
    return math.sqrt((a[0]-a[1])**2 + (b[0]-b[1])**2)


if __name__ == "__main__":
    points = [
        (0, 0), (4, 0), (4, 3), (0, 3)
    ]
    result = closest_pair(points)
    print(result)
