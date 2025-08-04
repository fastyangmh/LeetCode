from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[idx]] for idx in range(len(nums))]  # time O(n), space O(n)


if __name__ == '__main__':
    # ex1   ans [0,1,2,4,5,3]
    nums = [0, 2, 1, 5, 3, 4]
    print(Solution().buildArray(nums=nums))

    # ex2    ans [4,5,0,1,2,3]
    nums = [5, 0, 1, 2, 3, 4]
    print(Solution().buildArray(nums=nums))
