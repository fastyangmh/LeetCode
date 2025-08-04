from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        for idx in range(1, n):
            ans[idx] = ans[idx-1]*nums[idx-1]
        product = 1
        for idx in range(n-2, -1, -1):
            product *= nums[idx+1]
            ans[idx] = ans[idx]*product
        return ans


if __name__ == '__main__':
    # ex1    ans [24,12,8,6]
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums=nums))

    # ex2    ans [0,0,9,0,0]
    nums = [-1, 1, 0, -3, 3]
    print(Solution().productExceptSelf(nums=nums))
