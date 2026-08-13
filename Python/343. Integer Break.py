class Solution:
    def integerBreak(self, n: int) -> int:
        # # method1
        # dp = [0] * (n + 1)

        # for i in range(2, n + 1):
        #     for j in range(1, i):
        #         dp[i] = max(
        #             dp[i],
        #             j * (i - j),
        #             j * dp[i - j],
        #         )

        # return dp[-1]

        # method2
        if n == 2:
            return 1

        if n == 3:
            return 2

        remainder = n % 3

        if remainder == 0:
            return 3 ** (n // 3)

        if remainder == 1:
            return 3 ** ((n - 4) // 3) * 4

        if remainder == 2:
            return 3 ** ((n - 2) // 3) * 2
