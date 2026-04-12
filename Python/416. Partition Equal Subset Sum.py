class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # # method1
        # total = sum(nums)

        # if total % 2 != 0:
        #     return False

        # target = total // 2
        # n = len(nums)
        # dp = [[True] + [False] * target for _ in range(n + 1)]

        # for i in range(1, len(nums) + 1):
        #     num = nums[i - 1]

        #     for j in range(1, target + 1):
        #         dp[i][j] = dp[i - 1][j]

        #         if j >= num:
        #             dp[i][j] = dp[i][j] or dp[i - 1][j - num]

        # return dp[-1][-1]

        # method2
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[-1]
