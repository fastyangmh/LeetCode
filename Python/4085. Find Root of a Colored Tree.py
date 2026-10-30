class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        color_id = {"R": 0, "B": 1, "W": 2}

        degree = [0] * n
        indegree = [0] * n

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

            a, b = color_id[colors[u]], color_id[colors[v]]

            if a == b:
                return -1

            if (b - a) % 3 == 1:
                indegree[v] += 1
            else:
                indegree[u] += 1

        roots = [i for i in range(n) if indegree[i] == 0]

        if len(roots) != 1:
            return -1

        root = roots[0]

        return root if degree[root] <= 2 else -1
