from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # # method1
        # rows, cols = len(grid), len(grid[0])

        # def backtrack(ri, ci):
        #     if not (0 <= ri < rows and 0 <= ci < cols and grid[ri][ci] == 1):
        #         return 0

        #     grid[ri][ci] = 0

        #     return (
        #         1
        #         + backtrack(ri + 1, ci)
        #         + backtrack(ri - 1, ci)
        #         + backtrack(ri, ci + 1)
        #         + backtrack(ri, ci - 1)
        #     )

        # ans = 0

        # for ri in range(rows):
        #     for ci in range(cols):
        #         ans = max(ans, backtrack(ri, ci))

        # return ans

        # method2
        rows, cols = len(grid), len(grid[0])

        def backtrack(ri, ci):
            queue = deque([(ri, ci)])

            area = 0

            while queue:
                ri, ci = queue.popleft()

                if not (0 <= ri < rows and 0 <= ci < cols and grid[ri][ci] == 1):
                    continue
                grid[ri][ci] = 0
                area += 1
                queue.append((ri + 1, ci))
                queue.append((ri - 1, ci))
                queue.append((ri, ci + 1))
                queue.append((ri, ci - 1))

            return area

        ans = 0

        for ri in range(rows):
            for ci in range(cols):
                ans = max(ans, backtrack(ri, ci))

        return ans
