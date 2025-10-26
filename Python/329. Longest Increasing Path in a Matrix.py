from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            max_len = 1

            for dr, dc in directions:
                if (
                    not 0 <= r + dr < m
                    or not 0 <= c + dc < n
                    or matrix[r + dr][c + dc] <= matrix[r][c]
                ):
                    continue

                length = 1 + dfs(r + dr, c + dc)
                max_len = max(max_len, length)

            memo[r][c] = max_len

            return max_len

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans
