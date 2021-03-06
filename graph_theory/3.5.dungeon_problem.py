from typing import Tuple, List
from queue import SimpleQueue as Queue


def shortest_path(
    start: Tuple[int, int], end: Tuple[int, int], grid: List[List[int]]
) -> List[int]:
    num_rows = len(grid)
    num_cols = len(grid[0])
    grid_size = num_rows * num_cols
    ancestors = [None for _ in range(grid_size)]
    visited = [False for _ in range(grid_size)]
    if start == end:
        return [start]
    if grid[start[0]][start[1]] == 1:
        print("invalid start position")
        return []
    if grid[end[0]][end[1]] == 1:
        print("invalid end position")
        return []

    def bfs(start) -> List[int]:
        nonlocal grid
        nonlocal ancestors
        nonlocal visited
        nonlocal num_rows
        nonlocal num_cols
        q = Queue()
        q.put(start)
        visited[coordinate_to_index(start, num_rows, num_cols)] = True
        while not q.empty():
            position = q.get()
            neighbors = get_neighbors(position, grid)
            for neighbor in neighbors:
                if (
                    grid[neighbor[0]][neighbor[1]] == 0
                    and not visited[coordinate_to_index(neighbor, num_rows, num_cols)]
                ):
                    q.put(neighbor)
                    visited[coordinate_to_index(neighbor, num_rows, num_cols)] = True
                    ancestors[
                        coordinate_to_index(neighbor, num_rows, num_cols)
                    ] = position
        return ancestors

    ancestor_array = bfs(start)
    return build_path(start, end, ancestor_array, num_rows, num_cols)


def get_neighbors(
    position: Tuple[int, int], grid: List[List[int]]
) -> List[Tuple[int, int]]:
    # north south west east
    result = []
    row_offset = [-1, 1, 0, 0]
    col_offset = [0, 0, -1, 1]
    cardinal_directions = 4
    for i in range(cardinal_directions):
        r = position[0] + row_offset[i]
        c = position[1] + col_offset[i]
        if r > -1 and r < len(grid) and c > -1 and c < len(grid[0]):
            if grid[r][c] == 0:
                result.append((r, c))
    return result


def coordinate_to_index(coord: Tuple[int, int], num_rows: int, num_cols: int) -> int:
    return coord[1] + coord[0] * num_cols


def build_path(
    start: Tuple[int, int],
    end: Tuple[int, int],
    ancestor_array: List[int],
    num_rows: int,
    num_cols: int,
) -> List[int]:
    path = []
    iterator = end
    while True:
        path.append(iterator)
        if iterator == start:
            break
        ancestor = ancestor_array[coordinate_to_index(iterator, num_rows, num_cols)]
        iterator = ancestor
    path = list(reversed(path))
    return path


if __name__ == "__main__":
    from pprint import pprint

    dungeon = [
        [0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0],
    ]
    start = (0, 0)
    end = (4, 1)
    print(shortest_path(start, end, dungeon))
