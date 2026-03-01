class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        diff = 0
        sign = 1

        for idx, point in enumerate(nums):
            if point % 2 == 1:
                sign *= -1

            if idx % 6 == 5:
                sign *= -1

            diff += sign * point

        return diff
