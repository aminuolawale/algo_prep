# given n strings, find the  longest common substring that appears in at least k of the strings?

# Algorithm:
# concatenate the strings with sentinels
# sort the suffix array and build an longest common prefix array
# create a dynamic sliding window of width >= k on the lcp and check  if we have members from each string, 
#  we achieve this by associating each index on the lcp with the correponding string of which is the substring at the current index
# we find the minimum in each sliding window, ignoring the first element and keep the associated substring.
# The current kept substring by the time we get to the end of the lcp is the longest common substring. 





#### needs overhaul!!!!
from random import randint
from typing import List
def longest_common_substring(ss:List[str], r)-> str:
    agg = ""
    k = 58
    sents = set()
    print(ss)
    for i,s in enumerate(ss):
        agg += s
        agg += chr(k)
        sents.add(chr(k))
        k += 1
    suffix_array = []
    color = 0
    for i, l in enumerate(agg):
        if l in sents:
            color += 1
            continue
        suffix_array.append((i,agg[i:], color))
    colors = len(ss)
    suffix_array = sorted(suffix_array, key = lambda a: agg[a[0]:])
    lcp = [0 for _ in suffix_array]
    index = 1
    while index < len(lcp):
        prev = suffix_array[index-1][1]
        curr = suffix_array[index][1]
        color = suffix_array[index][2]
        k = 0
        while k < len(min(prev, curr, key= len)):
            if prev[k] != curr[k]:
                break
            k += 1
        lcp[index] = k
        index += 1
    start = 0
    end  = 0
    haves = {}
    longest = float("-inf")
    longest_string = ""
    color = suffix_array[end][2]
    haves.update({color:1})
    while end < len(lcp):
        if len(haves) < r:
            end += 1
            if end >= len(lcp):
                break
            color = suffix_array[end][2]
            if not color in haves:
                haves[color] = 0
            haves[color] += 1
        else:
            w = float("inf")
            ik = ""
            for b,h in enumerate(lcp[start+1:end + 1]):
                if h < w:
                    w = h
                    ik = suffix_array[start+b+1][1][:w]
            longest = max(w, longest)
            longest_string = max(ik, longest_string, key=len)
            # print(start, suffix_array)
            start_color = suffix_array[start][2]
            haves[start_color] -= 1
            if haves[start_color]== 0:
                del haves[start_color]
            start += 1
    return longest, longest_string





if __name__ == "__main__":
    ss = ["aabc", "bcdc", "bcde", "cded"]
    print(longest_common_substring(ss, 2))