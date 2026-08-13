class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[-1] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, 2 * n - 1):
            new_dp = [[-1] * n for _ in range(n)]

            row_min = max(0, k - (n - 1))
            row_max = min(k, n - 1)

            for r1 in range(row_min, row_max + 1):
                c1 = k - r1

                if grid[r1][c1] == -1:
                    continue

                for r2 in range(row_min, row_max + 1):
                    c2 = k - r2

                    if grid[r2][c2] == -1:
                        continue

                    best = -1

                    best = max(best, dp[r1][r2])

                    if r1 > 0:
                        best = max(best, dp[r1 - 1][r2])

                    if r2 > 0:
                        best = max(best, dp[r1][r2 - 1])

                    if r1 > 0 and r2 > 0:
                        best = max(best, dp[r1 - 1][r2 - 1])

                    if best == -1:
                        continue

                    cherries = grid[r1][c1]

                    if r1 != r2:
                        cherries += grid[r2][c2]

                    new_dp[r1][r2] = best + cherries
            dp = new_dp

        return max(0, dp[-1][-1])
