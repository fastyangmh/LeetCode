from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start, comb):
            if len(comb) >= k:
                res.append(comb)
                return

            for idx in range(start, n + 1):
                dfs(idx + 1, comb + [idx])

            return res

        return dfs(1, [])
