from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_combinations(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if total > target or idx >= len(candidates):
                return

            # left path (include)
            comb.append(candidates[idx])
            make_combinations(idx, comb, total + candidates[idx])

            # right path (not include)
            comb.pop()
            make_combinations(idx + 1, comb, total)

            return res

        return make_combinations(0, [], 0)
