class Solution:
    def rob(self, nums: List[int]) -> int:
        # # method1
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])

        # for idx in range(2, len(nums)):
        #     dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])

        # return dp[-1]

        # method2
        if len(nums) == 1:
            return nums[0]

        pre_prev = nums[0]
        prev = max(pre_prev, nums[1])

        for idx in range(2, len(nums)):
            curr = max(prev, pre_prev + nums[idx])
            pre_prev, prev = prev, curr

        return prev
