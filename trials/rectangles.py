#!/usr/bin/python3
def rectangles(arr: list) -> int:
    """ """
    for i, c in enumerate(arr):
        if c 
    return 1



def sort_coords(arr: list) -> list:
    """ """
    return sorted(sorted(arr, key=lambda a: a[0]), key=lambda a: a[1])


if __name__ == "__main__":
    arr = [
        (2, 0),
        (0, 0),
        (2, 2),
        (2, 3),
        (0, 1),
        (2, 1),
        (-1, 3),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
    ]
    ans = rectangles(arr)
    print(ans)