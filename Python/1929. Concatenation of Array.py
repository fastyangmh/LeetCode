from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n*2
        for idx in range(n):
            ans[idx] = nums[idx]
            ans[idx+n] = nums[idx]
        return ans


if __name__ == '__main__':
    # ex1    ans [1,2,1,1,2,1]
    nums = [1, 2, 1]
    print(Solution().getConcatenation(nums=nums))

    # ex2    ans [1,3,2,1,1,3,2,1]
    nums = [1, 3, 2, 1]
    print(Solution().getConcatenation(nums=nums))
