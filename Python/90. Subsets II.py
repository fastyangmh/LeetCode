class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue
                path.append(nums[idx])
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])

        return res
