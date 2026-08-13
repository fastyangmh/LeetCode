from collections import deque


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        INF = float("inf")
        dist1 = [INF] * (n + 1)
        dist2 = [INF] * (n + 1)

        dist1[1] = 0

        queue = deque([(1, 0)])

        while queue:
            node, d = queue.popleft()

            for nei in graph[node]:
                nd = d + 1

                if nd < dist1[nei]:
                    dist2[nei] = dist1[nei]
                    dist1[nei] = nd

                    queue.append((nei, nd))
                elif dist1[nei] < nd < dist2[nei]:
                    dist2[nei] = nd

                    queue.append((nei, nd))

        steps = dist2[n]
        current_time = 0

        for _ in range(steps):
            if (current_time // change) % 2 == 1:
                current_time = (current_time // change + 1) * change

            current_time += time

        return current_time
