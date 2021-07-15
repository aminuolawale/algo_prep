def bigSorting(arr):
    return sorted(sorted(arr), key=lambda a: len(a))


if __name__ == "__main__":
    arr = [
        str(a) for a in [1, 200, 1000, 3, 1400, 233, 2, 1030, 1020, 1120, 1121, 1021]
    ]
    ans = bigSorting(arr)
    print("the ans", ans)