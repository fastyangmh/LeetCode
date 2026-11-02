class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def backtrack(start, path, total):
            if total == target:
                ans.append(path[:])
                return

            if total > target:
                return

            for idx in range(start, len(candidates)):
                x = candidates[idx]

                path.append(x)
                backtrack(idx, path, total + x)
                path.pop()

        backtrack(0, [], 0)

        return ans
