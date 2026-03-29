class Solution:
    def rob(self, nums: List[int]) -> int:
        # # method1
        # if len(nums) == 1:
        #     return nums[0]

        # def solve(nums):
        #     if len(nums) == 1:
        #         return nums[0]

        #     n = len(nums)
        #     dp = [0] * n
        #     dp[0] = nums[0]
        #     dp[1] = max(nums[0], nums[1])

        #     for idx in range(2, n):
        #         dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])

        #     return dp[-1]

        # return max(
        #     solve(nums[:-1]),
        #     solve(nums[1:]),
        # )

        # method2
        if len(nums) == 1:
            return nums[0]

        def solve(nums):
            prev2 = prev1 = 0

            for num in nums:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            solve(nums[:-1]),
            solve(nums[1:]),
        )
