class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        connections = n - 1
        parent = list(range(n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px != py:
                parent[py] = px
                return True

            return False

        for t, u, v in logs:
            if union(u, v):
                connections -= 1

            if connections == 0:
                return t

        return -1
