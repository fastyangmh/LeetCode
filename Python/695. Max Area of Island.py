from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # method1
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                return 0

            grid[r][c] = -1

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                ans = max(ans, dfs(r, c))

        return ans

        # # method2
        # rows, cols = len(grid), len(grid[0])
        # ans = 0

        # def bfs(r, c):
        #     queue = deque([(r, c)])
        #     area = 0

        #     while queue:
        #         r, c = queue.popleft()

        #         if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
        #             continue

        #         grid[r][c] = -1
        #         area += 1
        #         queue.append((r + 1, c))
        #         queue.append((r - 1, c))
        #         queue.append((r, c + 1))
        #         queue.append((r, c - 1))

        #     return area

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] != 1:
        #             continue
        #         ans = max(ans, bfs(r, c))

        # return ans
