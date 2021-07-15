#  Knuth morris pratt pattern matching (substring search):
# (O(m+n))

# Algorithm:
# build a prefix array for the pattern:
# iterate through the pattern and the given string with their respective pointers.
# if there is a match increment both pointers
#  if no match move to the position stored in the j-ith position in the prefix array (why does this work though?)
# we have found the substring if j reaches the end of the pattern.
from typing import List
  


def kmp(s:str, t:str)-> int:
    pref_arr = prefix_array(t)
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            if j>0:
                ret_ind = pref_arr[j-1]
                j  = ret_ind
            else:
                i += 1
        else:
            i += 1
            j += 1
    return j == len(t)






def prefix_array(s:str)->List[int]:
    i = 0 
    j = 1
    res = [0 for _ in s]
    while j < len(s):
        if s[i] == s[j]:
            res[j] = 1 + res[j-1]
            i += 1
        else:
            i = 0
        j += 1
    return res



if __name__ == "__main__":
    s = "abxabcabcaby"
    t = "abcaby"
    print(kmp(s,t))
