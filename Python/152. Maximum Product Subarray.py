class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # method1
        # n = len(nums)
        # max_prod = [0] * n
        # min_prod = [0] * n

        # max_prod[0] = nums[0]
        # min_prod[0] = nums[0]
        # ans = nums[0]

        # for idx in range(1, n):
        #     max_prod[idx] = max(
        #         nums[idx], nums[idx] * max_prod[idx - 1], nums[idx] * min_prod[idx - 1]
        #     )
        #     min_prod[idx] = min(
        #         nums[idx], nums[idx] * max_prod[idx - 1], nums[idx] * min_prod[idx - 1]
        #     )

        #     ans = max(ans, max_prod[idx])

        # return ans

        # method2
        curr_max = curr_min = ans = nums[0]

        for idx in range(1, len(nums)):
            num = nums[idx]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)

            ans = max(ans, curr_max)

        return ans
