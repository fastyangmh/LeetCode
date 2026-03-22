class Solution:
    def climbStairs(self, n: int) -> int:
        # # method1
        # dp = [0] * (n + 1)
        # dp[0] = dp[1] = 1

        # for idx in range(2, len(dp)):
        #     dp[idx] = dp[idx - 1] + dp[idx - 2]

        # return dp[-1]

        # method2
        prev = curr = 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr
