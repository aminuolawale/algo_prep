def array_num(arr: list) -> list:

    prev = 1
    index = len(arr) - 1
    while True:
        arr[index] += prev
        a = arr[index] // 10
        b = arr[index] % 10
        arr[index] = b
        if a == 0:
            return arr
        if index == 0:
            if a > 0:
                arr = [a] + arr
            return arr
        prev = a
        index -= 1
    return arr


if __name__ == "__main__":
    print(array_num([9, 9, 9, 9, 9]))
