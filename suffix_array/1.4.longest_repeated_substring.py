#  return the longest substring that occurs more than once in a given string

# algorithm:
# construct the lcp;
# find the maximum value in the lcp
# return substring of substring of length equal to the value at  the current index of the lcpq  

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
    return lcparr, suffar

def lrs(s):
    lcparr, suffar = lcp(s)
    print(suffar)
    print(lcparr)
    m = float("-inf")
    mm = ""
    for i,l in enumerate(lcparr):
        if l > m:
            m = l
            mm = suffar[i-1][:l]

    return mm



print(lrs("akfldajkdfajdlkfasjfdklfajslkfjdsalkfjfioehaosfdlafjfiodfqhoeifas"))