class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if left == n or nums[left] != target:
            return [-1, -1]

        start = left

        right = n - 1

        while left < right:
            mid = (left + right + 1) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        end = left

        return [start, end]
