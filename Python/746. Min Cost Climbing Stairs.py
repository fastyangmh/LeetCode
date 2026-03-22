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
        prev2 = prev1 = 0

        for idx in range(2, len(cost) + 1):
            curr = min(
                prev2 + cost[idx - 2],
                prev1 + cost[idx - 1],
            )

            prev2 = prev1
            prev1 = curr

        return prev1
