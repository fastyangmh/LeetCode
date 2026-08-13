class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        INF = float("inf")

        n = len(points)

        min_dist = [INF] * n
        min_dist[0] = 0

        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            curr = -1

            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i

            visited[curr] = True
            total_cost += min_dist[curr]

            x1, y1 = points[curr]

            for nxt in range(n):
                if visited[nxt]:
                    continue

                x2, y2 = points[nxt]
                d = abs(x1 - x2) + abs(y1 - y2)

                min_dist[nxt] = min(min_dist[nxt], d)

        return total_cost
