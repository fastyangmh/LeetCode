class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        max_sum = float("-inf")
        left = 0

        for right, x in enumerate(nums):
            window_sum += x

            if right - left + 1 > k:
                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

        return max_sum / k
