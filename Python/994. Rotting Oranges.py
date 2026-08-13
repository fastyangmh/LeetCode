from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        fresh = 0
        starts = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    starts.append((r, c))

        if fresh == 0:
            return 0

        queue = deque(starts)
        minutes = 0

        while queue and fresh > 0:
            minutes += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

        return minutes if fresh == 0 else -1
