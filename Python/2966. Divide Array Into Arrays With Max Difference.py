from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        results = []

        for idx in range(0, len(nums), 3):
            if nums[idx + 2] - nums[idx] > k:
                return []

            results.append([nums[idx], nums[idx + 1], nums[idx + 2]])

        return results
