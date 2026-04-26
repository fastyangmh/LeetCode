from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # # method 1 O(n log n)
        # if len(nums) == 1:
        #     return 0
        # elif len(nums) == 2:
        #     return 0 if nums[0] > nums[1] else 1

        # l = len(nums) // 2

        # left = self.findPeakElement(nums[:l])
        # right = self.findPeakElement(nums[l:]) + l

        # return left if nums[left] > nums[right] else right

        # # method2 O(n)
        # l = len(nums)

        # for idx in range(l - 1):
        #     if nums[idx] > nums[idx + 1]:
        #         return idx
        # return l - 1

        # method3 O(log n)
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m

        return l