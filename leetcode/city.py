from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = sorted(m[0] for m in costs)
        b = sorted(m[1] for m in costs)
        print(a, b)
        return sum(a[: len(costs)]) + sum(b[: len(costs)])


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
