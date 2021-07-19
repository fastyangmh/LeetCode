from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_length = len(nums)+1
        ans = set(range(nums_length))-set(nums)
        return ans.pop()

        ''' my other solution, this is best
        nums_length = len(nums)+1
        sum_of_nums = nums_length*(nums_length-1)/2
        return int(sum_of_nums)-sum(nums)
        '''


if __name__ == '__main__':
    # ex1    ans 2
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums=nums))

    # ex2    ans 2
    nums = [0, 1]
    print(Solution().missingNumber(nums=nums))

    # ex3    ans 8
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(Solution().missingNumber(nums=nums))

    # ex4    ans 1
    nums = [0]
    print(Solution().missingNumber(nums=nums))
