class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        s_counter = Counter(list(s))
        s_chars = set(s)
        sorted_part = []
        rest = []
        for l in order:
            if l in s_counter:
                for i in range(s_counter[l]):
                    sorted_part.append(l)
                s_chars.remove(l)
        for l in list(s_chars):
            for i in range(s_counter[l]):
                rest.append(l)
        return "".join(sorted_part + rest)
    
if __name__ == "__main__":
    assert(Solution().customSortString("rastv", "avms") == "asvm")