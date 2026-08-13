class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # method1 time: O(mn), space: O(mn)
        # if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        #     return 0

        # rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # dp = [[0] * cols for _ in range(rows)]
        # dp[0][0] = 1

        # for r in range(1, rows):
        #     dp[r][0] = dp[r - 1][0] if obstacleGrid[r][0] == 0 else 0

        # for c in range(1, cols):
        #     dp[0][c] = dp[0][c - 1] if obstacleGrid[0][c] == 0 else 0

        # for r in range(1, rows):
        #     for c in range(1, cols):
        #         if obstacleGrid[r][c] == 1:
        #             dp[r][c] = 0
        #         else:
        #             dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # return dp[-1][-1]

        # method2
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1

        for c in range(1, cols):
            dp[c] = dp[c - 1] if obstacleGrid[0][c] == 0 else 0

        for r in range(1, rows):
            if obstacleGrid[r][0] == 1:
                dp[0] = 0

            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] = dp[c] + dp[c - 1]

        return dp[-1]
