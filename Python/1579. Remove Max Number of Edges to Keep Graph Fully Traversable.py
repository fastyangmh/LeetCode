class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n + 1))
                self.components = n

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])

                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)

                if px == py:
                    return False

                self.parent[py] = px

                self.components -= 1

                return True

        alice = UnionFind(n)
        bob = UnionFind(n)
        used = 0

        for t, u, v in edges:
            if t == 3 and alice.union(u, v):
                bob.union(u, v)
                used += 1

        for t, u, v in edges:
            if t == 1 and alice.union(u, v):
                used += 1

        for t, u, v in edges:
            if t == 2 and bob.union(u, v):
                used += 1

        if alice.components != 1 or bob.components != 1:
            return -1

        return len(edges) - used
