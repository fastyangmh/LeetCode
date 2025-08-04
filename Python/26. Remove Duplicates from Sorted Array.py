from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for v in nums:
            if v != nums[idx]:
                idx += 1
                nums[idx] = v
        return idx + 1


if __name__ == '__main__':
    #ex1    ans:    2, nums = [1,2,_]
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums=nums))

    #ex2    ans:    5, nums = [0,1,2,3,4,_,_,_,_,_]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums=nums))
