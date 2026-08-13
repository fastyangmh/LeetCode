import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        elevations = [[float("inf")] * cols for _ in range(rows)]
        elevations[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while pq:
            e, r, c = heapq.heappop(pq)

            if e > elevations[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return e

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                new_e = max(e, grid[nr][nc])

                if new_e >= elevations[nr][nc]:
                    continue

                elevations[nr][nc] = new_e

                heapq.heappush(pq, (new_e, nr, nc))

        return -1
