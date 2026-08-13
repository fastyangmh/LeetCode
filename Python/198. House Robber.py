class Solution:
    def rob(self, nums: List[int]) -> int:
        # # method1
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for idx in range(2, len(nums)):
        #     dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])

        # return dp[-1]

        # method2
        prev_prev = prev = 0

        for money in nums:
            prev_prev, prev = prev, max(prev, prev_prev + money)

        return prev
