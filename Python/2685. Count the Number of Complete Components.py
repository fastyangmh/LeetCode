from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(start):
            visited[start] = True

            stack = [start]
            nodes = 0
            degree = 0

            while stack:
                node = stack.pop()
                nodes += 1
                degree += len(graph[node])

                for nei in graph[node]:
                    if visited[nei]:
                        continue

                    visited[nei] = True
                    stack.append(nei)

            return nodes, degree // 2

        completed_count = 0

        for node in range(n):
            if visited[node]:
                continue

            nodes, edges = dfs(node)

            if edges == nodes * (nodes - 1) // 2:
                completed_count += 1

        return completed_count
