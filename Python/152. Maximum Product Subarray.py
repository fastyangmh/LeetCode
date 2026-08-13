class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = curr_min = curr_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curr_min, curr_max = curr_max, curr_min

            curr_min = min(num, curr_min * num)
            curr_max = max(num, curr_max * num)

            ans = max(ans, curr_max)

        return ans
