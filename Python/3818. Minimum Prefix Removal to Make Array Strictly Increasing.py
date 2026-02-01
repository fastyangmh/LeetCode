class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        # # mine
        # if len(nums) == 1:
        #     return 0

        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2

        #     if (
        #         sum(
        #             [
        #                 1
        #                 for idx in range(mid + 1, len(nums))
        #                 if nums[idx] > nums[idx - 1]
        #             ]
        #         )
        #         >= len(nums) - mid - 1
        #     ):

        #         r = mid - 1
        #     else:
        #         l = mid + 1

        # return l

        # method2
        idx = len(nums) - 1

        while idx > 0 and nums[idx] > nums[idx - 1]:
            idx -= 1

        return idx
