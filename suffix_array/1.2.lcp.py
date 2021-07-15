

def lcp(s:str):
    suffar = []
    for i, _ in enumerate(s):
        suffar.append(s[i:])
    lcparr = [0 for _ in suffar]
    suffar = sorted(suffar)
    index = 1
    while index < len(lcparr):
        prev = suffar[index-1]
        curr = suffar[index]
        k = 0
        while k < len(min(prev, curr, key= len)):
            if prev[k] != curr[k]:
                break
            k += 1
            
        lcparr[index] = k
        index += 1
    return lcparr

NAME = __name__
MAIN = "__main__"


if NAME == MAIN:
    s = "AZAZA"
    print(lcp(s))
