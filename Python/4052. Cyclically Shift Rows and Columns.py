class Solution:
    def cyclicShift(
        self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]
    ) -> list[list[int]]:
        ans = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                r = (i + colShift[j]) % n
                c = (j + rowShift[r]) % n

                ans[i][j] = grid[r][c]

        return ans
