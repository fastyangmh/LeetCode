from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # # method1
        # n = len(isConnected)
        # visited = set()
        # num_provinces = 0

        # def dfs(i):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and j not in visited:
        #             visited.add(j)
        #             dfs(j)

        # for i in range(n):
        #     if i not in visited:
        #         num_provinces += 1
        #         visited.add(i)
        #         dfs(i)

        # return num_provinces

        # # method2
        # n = len(isConnected)
        # num_provinces = 0
        # visited = set()

        # for i in range(n):
        #     if i in visited:
        #         continue

        #     num_provinces += 1
        #     queue = deque([i])

        #     while queue:
        #         city = queue.popleft()

        #         for j in range(n):
        #             if isConnected[city][j] == 1 and j not in visited:
        #                 visited.add(j)
        #                 queue.append(j)

        # return num_provinces

        # method3
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)

            if root_x != root_y:
                parent[root_y] = root_x

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len(set(find(i) for i in range(n)))
