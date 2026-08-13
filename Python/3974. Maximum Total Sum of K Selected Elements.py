class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        ans = 0

        for idx in range(k):
            ans += nums[idx] * mul if mul > 1 else nums[idx]
            mul -= 1

        return ans
