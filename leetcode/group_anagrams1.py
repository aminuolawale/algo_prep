from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            ss = "".join(sorted(s))
            if not ss in seen:
                seen.update({ss: [s]})
            else:
                seen[ss].append(s)
        output = []
        for k in seen:
            entry = seen[k]
            output.append(entry)
        return output


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
