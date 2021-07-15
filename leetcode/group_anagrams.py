from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            if seen:
                saw = False
                for k in seen:
                    if self.anag(k, s):
                        seen[k].append(s)
                        saw = True
                        break
                if not saw:
                    seen[s] = []
            else:
                seen[s] = []
        output = []
        for k in seen:
            entry = [k]
            entry.extend(seen[k])
            output.append(entry)
        return output

    def anag(self, a, b):
        am = {}
        asize = 0
        for l in a:
            if not am.get(l):
                am[l] = 0
            am[l] += 1
            asize += 1
        bm = {}
        bsize = 0
        for l in b:
            if not bm.get(l):
                bm[l] = 0
            bm[l] += 1
            bsize += 1
        if asize >= bsize:
            d = am
            d1 = bm
        else:
            d = bm
            d1 = am
        ans = all([d.get(k) == d1.get(k) for k in d])
        return ans


strs = ["ddddddddddg", "dgggggggggg"]
print(Solution().groupAnagrams(strs))
