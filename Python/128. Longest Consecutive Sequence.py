class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        unique_nums = set(nums)

        for i in unique_nums:
            if i - 1 in unique_nums:
                continue

            j = i

            while j in unique_nums:
                j += 1

            ans = max(ans, j - i)

        return ans
