from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1 / v

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, v in graph[curr].items():
                if neighbor in visited:
                    continue

                ret = dfs(neighbor, target, visited)

                if ret != -1:
                    return ret * v

            return -1

        ans = []

        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, set()))

        return ans
