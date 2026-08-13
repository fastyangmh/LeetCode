class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        # method1
        components = [0]
        groups = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                groups += 1

            components.append(groups)

        return [components[u] == components[v] for u, v in queries]

        # # method2
        # parent = list(range(n))

        # def find(x):
        #     if x != parent[x]:
        #         parent[x] = find(parent[x])

        #     return parent[x]

        # def union(x, y):
        #     px, py = find(x), find(y)

        #     if px != py:
        #         parent[py] = px

        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] <= maxDiff:
        #         union(i - 1, i)

        # return [find(u) == find(v) for u, v in queries]
