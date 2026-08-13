from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # method1
        # ans = []
        # used = [False] * len(nums)

        # def backtrack(path):
        #     if len(path) == len(nums):
        #         return ans.append(path[:])

        #     for idx in range(len(nums)):
        #         if used[idx]:
        #             continue

        #         used[idx] = True
        #         path.append(nums[idx])
        #         backtrack(path)
        #         path.pop()
        #         used[idx] = False

        # backtrack([])

        # return ans

        # method2
        ans = []

        def backtrack(start):
            if start >= len(nums):
                ans.append(nums[:])
                return

            for idx in range(start, len(nums)):
                nums[start], nums[idx] = nums[idx], nums[start]
                backtrack(start + 1)
                nums[start], nums[idx] = nums[idx], nums[start]

        backtrack(0)

        return ans
