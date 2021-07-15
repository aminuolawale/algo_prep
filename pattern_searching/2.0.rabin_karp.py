# substring search
# rolling hash
from string import ascii_lowercase


def rabin_karp(s, t):
    prime = 3
    l = len(t)
    start = 0
    end  = l
    target_hash = chash(t, prime)
    start_hash = chash(s[start:end], prime)
    while end < len(s):
        if start_hash == target_hash and t == s[start:end]:
            return True
        start_hash -= ord(s[start])
        start_hash //= prime
        start_hash += ord(s[end]) * prime ** (l-1)
        start += 1
        end += 1
    return target_hash == start_hash


def chash(t, prime):
    res = 0
    for i,l in enumerate(t):
        res += ord(l) * prime**i
    return res

if __name__ == "__main__":
    s = "iusaoidfoiasudfosyut"
    t = "yut"
    print(rabin_karp(s,t))