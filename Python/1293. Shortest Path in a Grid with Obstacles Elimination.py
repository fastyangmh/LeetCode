from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        shortest_path = rows + cols - 2

        if k >= shortest_path:
            return shortest_path

        best = [[-1] * cols for _ in range(rows)]
        best[0][0] = k

        queue = deque([(0, 0, k)])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c, remaining = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return steps

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    new_remaining = remaining - grid[nr][nc]

                    if new_remaining < 0 or new_remaining <= best[nr][nc]:
                        continue

                    best[nr][nc] = new_remaining

                    queue.append((nr, nc, new_remaining))

            steps += 1

        return -1
