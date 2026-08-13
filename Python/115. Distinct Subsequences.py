class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # # method1
        # m, n = len(s), len(t)

        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # for i in range(m + 1):
        #     dp[i][0] = 1

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == t[j - 1]:
        #             select = dp[i - 1][j - 1]
        #             not_select = dp[i - 1][j]

        #             dp[i][j] = select + not_select
        #         else:
        #             not_select = dp[i - 1][j]

        #             dp[i][j] = not_select

        # return dp[-1][-1]

        # method2
        m, n = len(s), len(t)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            prev = dp[0]

            for j in range(1, n + 1):
                tmp = dp[j]

                if s[i - 1] == t[j - 1]:
                    select = prev
                    not_select = dp[j]
                    dp[j] = select + not_select

                prev = tmp

        return dp[-1]
