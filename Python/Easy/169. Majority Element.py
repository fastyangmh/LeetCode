from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hash_table = {}
        for v in nums:
            if v in hash_table:
                hash_table[v] += 1
            else:
                hash_table[v] = 1
            if hash_table[v] > n/2:
                return v

        '''
        majority, count = None, 0
        for v in nums:
            if count == 0:
                majority = v
            if majority == v:
                count += 1
            else:
                count -= 1
        return majority'''


if __name__ == '__main__':
    # ex1    ans    3
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums=nums))

    # ex2    ans 2
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums=nums))
