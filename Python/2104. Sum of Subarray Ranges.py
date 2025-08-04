from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0

        for left in range(len(nums)):
            min_num = None
            max_num = None
            for right in range(left, len(nums)):
                min_num = (
                    min(min_num, nums[right]) if min_num is not None else nums[right]
                )
                max_num = (
                    max(max_num, nums[right]) if max_num is not None else nums[right]
                )
                ans += max_num - min_num

        return ans


# The O(n) solution is very hard, not understand.
