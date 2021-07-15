from pprint import pprint
# from Jenny
# Construct a matrix, from the two strings preppending both with an empty space
# Iterate through each row and compare each corresponding character at an index along the row. 
# If they are the same set the value at the cell to 1 + the northwest value and point a vector in that direction. if not set it to the maximum of north and west values
# and point vector in that direction.
# We continue till the matrix is filled up
# We start at the end of the matrix. If the vector is oriented in the northwest we add the character and move in the vector direction. If the vector isn't then we just move in the vector's direction.
# We do this till we are back at the start of the matrix.
# We now have the longest subsequence.

# Why does this work though?

def longest_common_subsequence(a, b):
    rows = len(b) + 1
    cols = len(a) + 1
    store = [[0 for _ in range(cols)] for _ in range(rows)]
    offset = [[0 for _ in range(cols)] for _ in range(rows)]
    i = 1
    a = "0" + a
    b = "0" + b
    while i < rows:
        j = 1
        while j < cols:
            if b[i] == a[j]:
                store[i][j] = 1 + store[i-1][j-1]
                offset[i][j] = (-1, -1)
            else:
                p, q = max((i, j-1), (i-1,j), key= lambda a: store[a[0]][a[1]])
                store[i][j] = store[p][q]
                offset[i][j] = (p-i, q-j)
            j += 1
        i += 1
    longest = store[-1][-1]
    i = rows -1
    j = cols -1
    res = ""
    while i > 0 and j > 0:
        vec = offset[i][j]
        if vec == (-1, -1):
            res = b[i] + res
        i += vec[0]
        j += vec[1]
    return res , longest


if __name__ == "__main__":
    s1 = "abcdefkdklajdflkasdf"
    s2 = "xdefafdslkafdslkfajldjkj;lkjlkg"
    print(longest_common_subsequence(s1, s2))