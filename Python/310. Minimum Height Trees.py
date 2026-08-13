from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

            degree[u] += 1
            degree[v] += 1

        queue = deque([i for i, d in enumerate(degree) if d == 1])
        remaining = n

        while remaining > 2:
            leaf_count = len(queue)
            remaining -= leaf_count

            for _ in range(leaf_count):
                node = queue.popleft()

                for nei in graph[node]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        queue.append(nei)

        return list(queue)
