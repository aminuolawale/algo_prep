def sortedSum(a):
    sorted_a = sorted(a)
    sum = 0
    index = len(sorted_a)
    while index > 0:
        sum += f(sorted_a)
        sorted_a.remove(a[index - 1])
        index -= 1
    return sum % (10 ** 9 + 7)


def f(a):
    return sum([(i + 1) * s for i, s in enumerate(a)])


if __name__ == "__main__":
    print(sortedSum([5, 9]))
