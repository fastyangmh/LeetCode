from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        for idx in range(1, len(nums)):
            ans[idx] = ans[idx - 1] * nums[idx - 1]

        last_right = 1

        for idx in range(len(nums) - 1, -1, -1):
            ans[idx] *= last_right
            last_right *= nums[idx]

        return ans
