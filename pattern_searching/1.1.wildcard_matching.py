

def wildcard_matching(s, p):
    store = [
        [False for _ in range(len(p) +1)] for _ in range(len(s) + 1)
    ]
    for j, c in enumerate(store[0]):
        if j == 0 or (p[j-1] == '*' and j == 1):
            store[0][j] = True
    
    for i in range(1, len(s) +1):
        for j in range(1, len(p) + 1):
            if p[j-1] == s[i-1] or p[j-1] == "?":
                store[i][j] = store[i-1][j-1]
            elif p[j-1] == "*":
                store[i][j] = store[i][j-1] or store[i-1][j]

    print(store)
    return store[-1][-1]




if __name__ == "__main__":
    s = "xaylmz"
    p = "x?y*z"
    s = "bxb"
    p = "*"
    print(wildcard_matching(s, p))