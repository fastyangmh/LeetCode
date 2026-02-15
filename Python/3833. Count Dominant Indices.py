class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        count = 0

        for num in nums:
            total -= num
            n -= 1
            count += 1 if num * n > total else 0

        return count
