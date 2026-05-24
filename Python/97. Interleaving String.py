class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # # method1
        # m, n = len(s1), len(s2)

        # if m + n != len(s3):
        #     return False

        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True

        # for i in range(m + 1):
        #     for j in range(n + 1):
        #         if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
        #             dp[i][j] = True

        #         if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
        #             dp[i][j] = True

        # return dp[-1][-1]

        # method2
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]

                if j > 0:
                    dp[j] = dp[j] or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1]
