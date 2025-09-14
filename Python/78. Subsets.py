from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # method1
        # res = []

        # def backtrack(start, path):
        #     res.append(path[:])

        #     for i in range(start, len(nums)):
        #         path.append(nums[i])
        #         backtrack(i + 1, path)
        #         path.pop()

        # backtrack(0, [])

        # return res

        # method2
        n = len(nums)
        res = []

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)

        return res
