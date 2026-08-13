class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # method1
        # n = len(cost)
        # dp = [0] * (n + 1)

        # for idx in range(2, len(dp)):
        #     dp[idx] = min(
        #         dp[idx - 1] + cost[idx - 1],
        #         dp[idx - 2] + cost[idx - 2],
        #     )

        # return dp[-1]

        # method2
        n = len(cost)

        prev_prev = prev = 0

        for i in range(2, n + 1):
            prev_prev, prev = prev, min(prev_prev + cost[i - 2], prev + cost[i - 1])

        return prev
