from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(start, comb, total):
            if total == target:
                res.append(comb)
                return

            if total > target or start >= len(candidates):
                return

            for idx in range(start, len(candidates)):
                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue

                if total + candidates[idx] > target:
                    break

                dfs(idx + 1, comb + [candidates[idx]], total + candidates[idx])

        dfs(0, [], 0)
        return res
