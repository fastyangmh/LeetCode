class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = nums[len(nums) // 2]
        cnt = 0

        for x in nums:
            cnt += 1 if x == mid else 0
            if cnt > 1:
                return False

        return True
