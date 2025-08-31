from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # method1
        # return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)

        # # method2
        # res = len(nums)

        # for idx, n in enumerate(nums):
        #     res ^= idx ^ n

        # return res

        # method3
        res = len(nums)

        for idx, n in enumerate(nums):
            res += idx - n

        return res
