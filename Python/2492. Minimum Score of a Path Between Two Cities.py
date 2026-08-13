from collections import deque


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # method1
        graph = {}

        for u, v, w in roads:
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))

        queue = deque([1])
        ans = float("inf")
        visited = {1}

        while queue:
            city = queue.popleft()

            for next_city, dist in graph.get(city, []):
                ans = min(ans, dist)

                if next_city not in visited:
                    visited.add(next_city)
                    queue.append(next_city)

        return ans

        # # method2
        # parent = list(range(n + 1))

        # def find(x):
        #     if x != parent[x]:
        #         parent[x] = find(parent[x])

        #     return parent[x]

        # def union(x, y):
        #     px, py = find(x), find(y)

        #     if px != py:
        #         parent[py] = px

        # for u, v, _ in roads:
        #     union(u, v)

        # root = find(1)
        # ans = float("inf")

        # for u, _, w in roads:
        #     if find(u) == root:
        #         ans = min(ans, w)

        # return ans
