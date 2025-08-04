from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur = nums[0]
        res = nums[0]
        for idx in range(1, len(nums)):
            if cur < 0:  # max(nums[i-1]+nums[i], num[i])
                cur = nums[idx]
            else:
                cur += nums[idx]
            if cur > res:
                res = cur
        return res


if __name__ == '__main__':
    #ex1    6
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums=nums))

    #ex2    1
    nums = [1]
    print(Solution().maxSubArray(nums=nums))

    #ex3    23
    nums = [5, 4, -1, 7, 8]
    print(Solution().maxSubArray(nums=nums))
