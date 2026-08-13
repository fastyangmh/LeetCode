class Solution:
    def climbStairs(self, n: int) -> int:
        # # method1
        # dp = [0] * (n + 1)
        # dp[0] = dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[-1]

        # method2
        if n <= 2:
            return n

        prev2 = prev1 = 1

        for i in range(2, n + 1):
            prev2, prev1 = prev1, prev2 + prev1

        return prev1