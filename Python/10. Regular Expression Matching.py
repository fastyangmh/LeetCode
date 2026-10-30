class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # method1
        # m, n = len(s), len(p)

        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True

        # for j in range(2, n + 1):
        #     if p[j - 1] == "*":
        #         dp[0][j] = dp[0][j - 2]

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] != "*":
        #             if p[j - 1] == "." or p[j - 1] == s[i - 1]:
        #                 dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = dp[i][j - 2]

        #             if p[j - 2] == "." or p[j - 2] == s[i - 1]:
        #                 dp[i][j] = dp[i][j] or dp[i - 1][j]

        # return dp[m][n]

        # method2
        n = len(p)

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[j] = dp[j - 2]

        for i in range(1, len(s) + 1):
            prev = dp[0]
            dp[0] = False

            for j in range(1, n + 1):
                temp = dp[j]

                if p[j - 1] == "*":
                    dp[j] = dp[j - 2]

                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[j] = dp[j] or temp

                else:
                    match = p[j - 1] == "." or p[j - 1] == s[i - 1]
                    dp[j] = match and prev

                prev = temp

        return dp[n]
