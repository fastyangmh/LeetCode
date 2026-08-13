class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        zero_idx = -1

        for right, num in enumerate(nums):
            if num == 0:
                if zero_idx != -1:
                    left = zero_idx + 1

                zero_idx = right

            ans = max(ans, right - left + 1)

        return ans
