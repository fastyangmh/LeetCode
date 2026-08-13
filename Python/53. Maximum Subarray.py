class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = float("-inf")

        for x in nums:
            curr_sum = max(curr_sum + x, x)
            max_sum = max(max_sum, curr_sum)

        return max_sum
