from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, v in enumerate(nums):
            diff = target-v
            if diff in hash_table:
                return [hash_table[diff], idx]
            else:
                hash_table[v] = idx


if __name__ == '__main__':
    # ex1   [0,1]
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums=nums, target=target))

    #ex2    [1,2]
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums=nums, target=target))

    #ex3    [0,1]
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums=nums, target=target))
