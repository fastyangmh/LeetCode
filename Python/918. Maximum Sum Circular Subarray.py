class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        max_sum = curr_max = nums[0]
        min_sum = curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)

        if total - min_sum == 0:
            return max_sum

        return max(max_sum, total - min_sum)
