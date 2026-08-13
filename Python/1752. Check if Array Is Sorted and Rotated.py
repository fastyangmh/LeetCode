class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            count += 1 if nums[i] > nums[(i + 1) % n] else 0

        return count <= 1
