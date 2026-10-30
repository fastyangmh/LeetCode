from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        dp = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            max_len = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (
                    0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]
                ):
                    continue

                length = 1 + dfs(nr, nc)
                max_len = max(max_len, length)

            dp[r][c] = max(dp[r][c], max_len)

            return dp[r][c]

        ans = 0

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans
