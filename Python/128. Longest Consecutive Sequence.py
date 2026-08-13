class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = set(nums)
        ans = 0

        for x in unique:
            if x - 1 in unique:
                continue

            y = x

            while y in unique:
                y += 1

            ans = max(ans, y - x)

        return ans
