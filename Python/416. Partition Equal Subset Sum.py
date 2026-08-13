class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # # method1
        # total = sum(nums)

        # if total & 1:
        #     return False

        # target = total // 2
        # n = len(nums)

        # dp = [[False] * (target + 1) for _ in range(n + 1)]

        # for i in range(n + 1):
        #     dp[i][0] = True

        # for i in range(1, n + 1):
        #     for t in range(1, target + 1):
        #         num = nums[i - 1]

        #         dp[i][t] = dp[i - 1][t]

        #         if t >= num:
        #             dp[i][t] |= dp[i - 1][t - num]

        # return dp[-1][-1]

        # method2
        total = sum(nums)

        if total & 1:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] |= dp[t - num]

        return dp[-1]
