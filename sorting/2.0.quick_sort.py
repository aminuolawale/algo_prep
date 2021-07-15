


def quick_sort(arr):
    if len(arr) == 0:
        return []
    pivot = 0
    start = 0
    end = len(arr) -1
    print(arr)
    while True:
        while start < len(arr) and arr[start] <= arr[pivot] :
            start += 1
        while end < len(arr) and arr[end] > arr[pivot]:
            end -=1
        if not start < end:
            break
        arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot] = arr[pivot], arr[end]
    return quick_sort(arr[pivot:end]) + [arr[end]] + quick_sort(arr[end+1:])




if __name__ == "__main__":
    arr = [7,6,10,5,9,2,1,15,7, 23, 1, 35, 1, 13, -9]
    res = quick_sort(arr)
    print(res)
