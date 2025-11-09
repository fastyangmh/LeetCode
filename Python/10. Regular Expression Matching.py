class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # method1
        # if not p:
        #     return not s

        # first_match = bool(s) and (p[0] == "." or p[0] == s[0])

        # if len(p) >= 2 and p[1] == "*":
        #     return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))

        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])

        # method2
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            first = i < len(s) and (p[j] in {s[i], "."})
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = dfs(i, j + 2) or (first and dfs(i + 1, j))
            else:
                memo[(i, j)] = first and dfs(i + 1, j + 1)
            return memo[(i, j)]

        return dfs(0, 0)

        # # method3
        # m, n = len(s), len(p)
        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True

        # for j in range(2, n + 1):
        #     if p[j - 1] == "*":
        #         dp[0][j] = dp[0][j - 2]

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] in {s[i - 1], "."}:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         elif p[j - 1] == "*":
        #             dp[i][j] = dp[i][j - 2] or (
        #                 dp[i - 1][j] and (p[j - 2] in {s[i - 1], "."})
        #             )

        # return dp[m][n]

        # # method4
        # m, n = len(s), len(p)

        # prev = [False] * (n + 1)
        # curr = [False] * (n + 1)

        # prev[0] = True

        # for j in range(2, n + 1):
        #     if p[j - 1] == "*":
        #         prev[j] = prev[j - 2]

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] in {s[i - 1], "."}:
        #             curr[j] = prev[j - 1]
        #         elif p[j - 1] == "*":
        #             curr[j] = curr[j - 2] or (prev[j] and (p[j - 2] in {s[i - 1], "."}))
        #         else:
        #             curr[j] = False

        #     prev, curr = curr, [False] * (n + 1)

        # return prev[n]
