class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deleted = 0

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            deleted += 1 if a == b else 0

        return deleted
