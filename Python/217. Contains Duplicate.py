from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # method1
        # return len(set(nums)) < len(nums)

        # method2
        # nums.sort()

        # for idx in range(1, len(nums)):
        #     if nums[idx] == nums[idx - 1]:
        #         return True
        # return False

        # method3
        set_ = set()

        for n in nums:
            if n in set_:
                return True
            set_.add(n)

        return False
