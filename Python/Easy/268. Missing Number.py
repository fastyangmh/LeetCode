# import
from typing import List


# class
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)  # n*log(n)

        for idx, n in enumerate(sorted_nums):
            if idx != n:
                return idx
        return sorted_nums[-1] + 1


if __name__ == "__main__":
    # Example 1:
    nums = [3, 0, 1]
    assert Solution().missingNumber(nums) == 2, Solution().missingNumber(nums)

    # Example 2:
    nums = [0, 1]
    assert Solution().missingNumber(nums) == 2, Solution().missingNumber(nums)

    # Example 3:
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert Solution().missingNumber(nums) == 8, Solution().missingNumber(nums)
