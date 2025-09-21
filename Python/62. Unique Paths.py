class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # method1 time: O(m*n) space: O(m*n)
        # dp = [[1] * n for _ in range(m)]

        # for ri in range(1, m):
        #     for ci in range(1, n):
        #         dp[ri][ci] = dp[ri - 1][ci] + dp[ri][ci - 1]

        # return dp[-1][-1]

        # method2
        last_row = [1] * n

        for ri in range(1, m):
            for ci in range(1, n):
                last_row[ci] += last_row[ci - 1]

        return last_row[-1]
