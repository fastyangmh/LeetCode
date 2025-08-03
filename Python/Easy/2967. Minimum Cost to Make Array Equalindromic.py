from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        cost_func = lambda x: sum(abs(v - x) for v in nums)
        median = nums[len(nums) // 2]
        left, right = median - 1, median + 1

        while str(left) != str(left)[::-1]:
            left -= 1

        while str(right) != str(right)[::-1]:
            right += 1

        candidate = [left, right]

        if str(median) == str(median)[::-1]:
            candidate.append(median)

        return min(cost_func(v) for v in candidate)
