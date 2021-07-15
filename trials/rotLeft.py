def rotLeft(a, d):
    """ """
    index = 0
    themap = {}
    shift = d % len(a)
    while index < len(a):
        next_index = (index + shift) % len(a)
        themap[index] = a[index]
        if themap.get(next_index):
            a[index] = themap[next_index]
        else:
            a[index] = a[next_index]
        index += 1
    return a


print(rotLeft([1, 2, 3, 4, 5, 7], 4))
