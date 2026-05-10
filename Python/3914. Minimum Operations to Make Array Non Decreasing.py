class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0

        for i in range(len(nums) - 1):
            ans += max(0, nums[i] - nums[i + 1])

        return ans
