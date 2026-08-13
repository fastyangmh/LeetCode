class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        ans = 0
        window_sum = 0

        for right, num in enumerate(nums):
            window_sum += num

            while num * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans
