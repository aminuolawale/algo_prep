from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        start_pointer = 0
        end_pointer = len(sorted_nums) - 1
        while start_pointer != end_pointer:
            sum = sorted_nums[start_pointer] + sorted_nums[end_pointer]
            if sum < target:
                start_pointer += 1
            elif sum > target:
                end_pointer -= 1
            else:
                first_value = sorted_nums[start_pointer]
                second_value = sorted_nums[end_pointer]
                print(first_value, second_value)
                first_index = nums.index(first_value)
                nums[first_index] = None
                second_index = nums.index(second_value)
                return [first_index, second_index]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for index, element in enumerate(nums):
            print(element)
            if complement_map.get(element) is not None:
                return [complement_map.get(element), index]
            complement = target - element
            complement_map.update({complement: index})
            print(complement_map)
        return []


# print(Solution().twoSum1([-1, -2, -3, -4, -5], -8))
print(Solution().twoSum1([3, 3], 6))
