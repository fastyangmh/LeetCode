class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # method1
        # n = len(nums)
        # max_prod = [0] * n
        # min_prod = [0] * n
        # ans = max_prod[0] = min_prod[0] = nums[0]

        # for i in range(1, n):
        #     max_prod[i] = max(
        #         nums[i], max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i]
        #     )
        #     min_prod[i] = min(
        #         nums[i], max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i]
        #     )

        #     ans = max(ans, max_prod[i])

        # return ans

        # method2
        n = len(nums)
        ans = curr_max = curr_min = nums[0]

        for i in range(1, n):
            prev_max, prev_min = curr_max, curr_min

            curr_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            curr_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])

            ans = max(ans, curr_max)

        return ans
