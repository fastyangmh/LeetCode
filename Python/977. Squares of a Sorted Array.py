from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # time O(n*nlogn) space O(1)
        for idx in range(len(nums)):
            nums[idx] = nums[idx]**2
        nums = sorted(nums)
        return nums


if __name__ == '__main__':
    # ex1    ans [0,1,9,16,100]
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums=nums))

    # ex2    ans [4,9,9,49,121]
    nums = [-7, -3, 2, 3, 11]
    print(Solution().sortedSquares(nums=nums))
