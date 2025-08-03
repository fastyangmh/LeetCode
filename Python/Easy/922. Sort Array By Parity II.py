from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_idx = 1

        for even_idx in range(0, len(nums), 2):
            if nums[even_idx] % 2 != 0:
                while nums[odd_idx] % 2:
                    odd_idx += 2
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
        return nums
