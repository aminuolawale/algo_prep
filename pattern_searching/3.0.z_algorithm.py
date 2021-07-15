# find all the occurences of a substring in a given string.
#  The Z algrorithm is centered around the z array where z[k] is the length of the longest substring starting at k which is
#  also a prefix of the string. 
# We first create and aggregate string and by joining the pattern with the string separating them with a delimiter absent from both strings.
# the we construct a z array from the resulting string.
# after that, we resize the z array to its original size and accordingly, then we find all occurences of the lenght of the pattern in the resulting array,
# these represent the start positions of all the occurences of the substring in the array.
# We append the pattern to the beginning because of the nature of the construction of the aggregate string. (we are comparing with the prefix)
# why do we need the delimiter though?
#  We need it because in the case where the given string begins with the pattern, we run into the danger of a cycle where the pattern is continued by the string and and we keep 
# iterating and get a larger value than we should:
# consider s = "abcabc" and t = "abc"
# if we concatenate into u = "abcabcabc"
# our z array will become [0,0,0,6,0,0,3,0,0] instead of [0,0,0,3,0,0,3,0,0]

from typing import List

def z(s:str, t:str) -> List[int]:
    index = 1
    start  = 0
    s = t + "~" + s
    z = [0 for _ in s]
    while index < len(s):
        k = index
        while k < len(s) and s[k] == s[start]:
            k += 1
            start += 1
        print(start, index, k)
        z[index] = k - index
        index += 1
        start = 0
    z= z[len(t)+1:]
    return [i for i,v in enumerate(z) if v == len(t)]


if __name__ == "__main__":
    s = "aflkajhakjsahdjhkrrttxxafkdhfdhsahdfakfldajfkdslafdljkjrrttxxkfjaslkfjlsajdkrrttxxrrttxx"
    t  = "rrttxx"
    print(z(s,t))