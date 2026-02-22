class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return

            if start >= len(candidates):
                return

            for idx in range(start, len(candidates)):
                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue

                if total + candidates[idx] > target:
                    break

                path.append(candidates[idx])
                backtrack(idx + 1, path, total + candidates[idx])
                path.pop()

        backtrack(0, [], 0)

        return res
