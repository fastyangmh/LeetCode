class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # method1
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (target + total) % 2 == 1:
            return 0

        subset_sum = (target + total) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[-1]

        # # method2
        # memo = {}

        # def dfs(start, total):
        #     if start == len(nums):
        #         return 1 if total == target else 0

        #     if (start, total) in memo:
        #         return memo[(start, total)]

        #     res = dfs(start + 1, total + nums[start]) + dfs(
        #         start + 1, total - nums[start]
        #     )

        #     memo[(start, total)] = res

        #     return res

        # return dfs(0, 0)
