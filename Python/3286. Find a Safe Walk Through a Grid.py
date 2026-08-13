from collections import deque


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dist = [[float("inf")] * cols for _ in range(rows)]

        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                new_cost = dist[r][c] + grid[nr][nc]

                if new_cost >= dist[nr][nc] or new_cost >= health:
                    continue

                dist[nr][nc] = new_cost

                if grid[nr][nc] == 0:
                    dq.appendleft((nr, nc))
                else:
                    dq.append((nr, nc))

        return dist[-1][-1] < health
