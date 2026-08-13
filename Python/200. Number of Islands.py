from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # method1
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            grid[r][c] = "-1"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                    continue

                dfs(nr, nc)

        ans = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                ans += 1
                dfs(r, c)

        return ans

        # # method2
        # rows = len(grid)
        # cols = len(grid[0])

        # def bfs(ri, ci):
        #     grid[ri][ci] = "0"
        #     queue = [(ri, ci)]

        #     while queue:
        #         x, y = queue.pop(0)

        #         for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        #             nx, ny = x + dx, y + dy

        #             if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
        #                 grid[nx][ny] = "0"
        #                 queue.append((nx, ny))

        # count = 0

        # for ri in range(rows):
        #     for ci in range(cols):
        #         if grid[ri][ci] != "1":
        #             continue

        #         bfs(ri, ci)
        #         count += 1

        # return count
