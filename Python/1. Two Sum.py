class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, v in enumerate(nums):
            diff = target - v

            if diff in seen:
                return [seen[diff], i]

            seen[v] = i
