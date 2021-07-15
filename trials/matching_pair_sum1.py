def matching_pair_sum(array):
    """ """
    maps = {}
    for i, v in enumerate(array):
        if v == maps.get(8 - v):
            print(v, 8 - v)
            return "YES"
        maps.update({v: 8 - v})
    return "NO"


if __name__ == "__main__":
    array = [11, 23, 3, 4, 7, 6, -3]
    answer = matching_pair_sum(array)
    print("the answer", answer)
