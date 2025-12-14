from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for idx in range(1, n):
            ans[idx] = ans[idx - 1] * nums[idx - 1]

        last_right = 1

        for idx in range(n - 1, -1, -1):
            ans[idx] *= last_right
            last_right *= nums[idx]

        return ans
