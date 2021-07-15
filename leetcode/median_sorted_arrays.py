from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_pointer = -1
        second_pointer = -1
        index = 0
        current = None
        total_length = len(nums1) + len(nums2)
        is_even = total_length % 2 == 0
        while index < total_length // 2 + 1:
            previous = current
            if first_pointer + 1 < len(nums1):
                if second_pointer + 1 < len(nums2):
                    if nums1[first_pointer + 1] <= nums2[second_pointer + 1]:
                        first_pointer += 1
                        current = nums1[first_pointer]
                    else:
                        second_pointer += 1
                        current = nums2[second_pointer]
                else:
                    first_pointer += 1
                    current = nums1[first_pointer]
            elif second_pointer + 1 < len(nums2):
                second_pointer += 1
                current = nums2[second_pointer]
            index += 1
        if is_even:
            return float(previous + current) / 2

        return current


print(Solution().findMedianSortedArrays([2], []))
