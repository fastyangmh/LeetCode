class Solution:
    def climbStairs(self, n: int) -> int:
        # # method1
        # dp = [0] * (n + 1)
        # dp[0] = dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[-1]

        # method2
        prev = curr = 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr
