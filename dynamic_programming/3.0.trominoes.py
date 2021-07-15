

!!!!!!!!!!!!!!!wrong
# Come back to do
def tile_trominoes(n):
    rows = 2
    store = [
        [0 for _ in range(2**rows)] for _ in range(n+1)
    ]
    store[0][3] = 1
    print(store)
    for i in range(1, n+1):
        store[i][0] += store[i-1][3]

        store[i][1] += store[i-1][3]
        store[i][1] += store[i-1][2]


        store[i][2] += store[i-1][3]
        store[i][2] += store[i-1][1]

        store[i][3] += store[i-1][1]
        store[i][3] += store[i-1][2]
        store[i][3] += store[i-1][0]
        print(store)

    return store[n][3]







if __name__ == "__main__":
    print(tile_trominoes(3))