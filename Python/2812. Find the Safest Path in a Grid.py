from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        dist = [[-1] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                dist[r][c] = 0
                queue.append((r, c))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1):
                    continue

                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

        heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe

            if visited[r][c]:
                continue

            visited[r][c] = True

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n and not visited[nr][nc]):
                    continue

                new_safe = min(safe, dist[nr][nc])
                heapq.heappush(heap, (-new_safe, nr, nc))

        return 0
