class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, path, total):
            if total == target:
                ans.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                x = candidates[i]

                path.append(x)
                backtrack(i, path, total + x)
                path.pop()

        backtrack(0, [], 0)
        return ans
