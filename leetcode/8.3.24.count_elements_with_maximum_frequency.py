from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        max_freq = float("-inf")
        result = 0
        for _, freq in counter.items():
            if freq == max_freq:
                result += freq
            elif freq > max_freq:
                max_freq = result = freq
        return result
    
if __name__ == "__main__":
    assert(Solution().maxFrequencyElements([1,2,2,2,3,4,5,5,5]) == 6)

        