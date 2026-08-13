class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px != py:
                parent[py] = px

        for u, v in edges:
            union(u, v)

        return len(set(find(x) for x in range(n)))
