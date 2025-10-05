from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                continue

            nums[idx], nums[non_zero_idx] = nums[non_zero_idx], nums[idx]
            non_zero_idx += 1
