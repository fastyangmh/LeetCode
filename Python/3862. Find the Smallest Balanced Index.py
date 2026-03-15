class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        prev_sum = sum(nums)
        prev_prod = 1

        for idx in range(len(nums) - 1, -1, -1):
            prev_sum -= nums[idx]

            # when idx moves from right to left, the prod only becomes lager and
            # sum only becomes smaller
            if prev_prod > prev_sum:
                break

            if prev_sum == prev_prod:
                return idx

            prev_prod *= nums[idx]

        return -1
