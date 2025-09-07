from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # method1
        rows = len(grid)
        cols = len(grid[0])

        def dfs(ri, ci):
            if not (0 <= ri < rows and 0 <= ci < cols and grid[ri][ci] == "1"):
                return

            grid[ri][ci] = "0"

            dfs(ri - 1, ci)
            dfs(ri + 1, ci)
            dfs(ri, ci - 1)
            dfs(ri, ci + 1)

        count = 0

        for ri in range(rows):
            for ci in range(cols):
                if grid[ri][ci] != "1":
                    continue
                dfs(ri, ci)
                count += 1

        return count

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
