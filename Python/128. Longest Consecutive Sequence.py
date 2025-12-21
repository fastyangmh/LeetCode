from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = set(nums)
        result = 0

        for x in unique_nums:
            if x - 1 in unique_nums:
                continue

            y = x

            while y in unique_nums:
                y += 1

            result = max(result, y - x)

        return result
