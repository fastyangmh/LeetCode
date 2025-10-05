from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            while 1 <= nums[idx] < len(nums) and nums[nums[idx] - 1] != nums[idx]:
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]

        for idx, num in enumerate(nums):
            if idx + 1 != num:
                return idx + 1

        return len(nums) + 1
