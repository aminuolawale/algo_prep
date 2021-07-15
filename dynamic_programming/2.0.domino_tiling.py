# # In how many ways can you tile a 3 * N grid with 2 * 1 dominoes?
# each column can be in any of 8 states. 
# for each of these states we calculate how many ways we can arrive  at it using other states. 
# The base state is the number of columns is zero and we can only tile it in one way. The next reachable states are states
# 0, 4, 5, and with this we calculate other states iteratively til we have reached the last column in the question.

# !!!!! why don't my states 1 and 3 lead to 7 though, they just need one tile


def tile_dominoes(n):
    rows = 3
    cols = n
    store = [
        [0 for _ in range(2**rows)] for _ in range(cols +1)
    ]
    store[0][7] = 1
    for i in range(1, cols+1):
        store[i][0] += store[i-1][7]
    
        store[i][1] += store[i-1][5]

        # store[i][2] += store[i-1][6]

        store[i][3] += store[i-1][4]

        store[i][4] += store[i-1][7]
        store[i][4] += store[i-1][3]


        store[i][5] += store[i-1][7]
        store[i][5] += store[i-1][1]

        # store[i][6] += store[i-1][2]

        store[i][7] += store[i-1][5]
        store[i][7] += store[i-1][4]
        store[i][7] += store[i-1][0]
        
        

    return store[cols][7]
print(tile_dominoes(8))




        





