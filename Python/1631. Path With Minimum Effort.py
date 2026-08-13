import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = float("inf")
        rows, cols = len(heights), len(heights[0])

        cost = [[INF] * cols for _ in range(rows)]
        cost[0][0] = 0

        pq = [(0, 0, 0)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while pq:
            effort, r, c = heapq.heappop(pq)

            if effort > cost[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))

                if new_effort >= cost[nr][nc]:
                    continue

                cost[nr][nc] = new_effort

                heapq.heappush(pq, (new_effort, nr, nc))

        return -1
