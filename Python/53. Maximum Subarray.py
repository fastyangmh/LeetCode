from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for idx in range(1, len(nums)):
            curr_sum = max(nums[idx], curr_sum + nums[idx])
            max_sum = max(max_sum, curr_sum)

        return max_sum
