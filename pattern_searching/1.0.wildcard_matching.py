# T[i][j] = T[i-1][j-1] if s[i] == p[j]  or p[j] == "?"
#          = T[i-1][j] or T[i][j-1] if p[j] == "*"
#           = False 
# Propulate first row and column with comparison of null string vs full pattern and null pattern vs full string.
# revise without preppending the string.
import re

def wild_card_matching(s, p):  
    s = "~" + s
    p  = "~" + re.sub("\*+","*", p)
    print(p)
    store = [
        [False for _ in p] for _ in s 
    ]
    for j,l in enumerate(p):
        store[0][j] = s[0] == p[:j+1] or p[1] == "*"

    for i, l in enumerate(s):
        store[i][0] = p[0] == s[:i+1]

    for i, row in enumerate(store):
        for j, col in enumerate(row):
            if i < 1 or j < 1:
                continue
            if s[i] == p[j] or p[j] == "?":
                store[i][j] = store[i-1][j-1] 
            elif p[j] == "*":
                store[i][j] = store[i-1][j] or store[i][j-1] 
    print(store)
    return store[-1][-1]



if __name__ == "__main__":
    s = "xaylmz"
    p = "x?y*z"
    s = "bxb"
    p = "b************************************?b"
    print(wild_card_matching(s, p))