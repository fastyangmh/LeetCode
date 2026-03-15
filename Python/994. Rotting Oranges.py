from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for ri in range(rows):
            for ci in range(cols):
                if grid[ri][ci] == 2:
                    queue.append((ri, ci))
                elif grid[ri][ci] == 1:
                    fresh += 1

        minute = 0

        while queue and fresh > 0:
            minute += 1

            for _ in range(len(queue)):
                ri, ci = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = ri + dr, ci + dc

                    if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

        return minute if fresh == 0 else -1
