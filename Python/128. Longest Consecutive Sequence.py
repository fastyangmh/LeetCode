from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = set(nums)
        ret = 0

        for num in unique_nums:
            if num - 1 in unique_nums:
                continue

            count = 1

            while num + 1 in unique_nums:
                count += 1
                num += 1

            ret = max(ret, count)

        return ret
