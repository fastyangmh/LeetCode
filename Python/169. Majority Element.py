from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # method1
        # nums.sort()

        # return nums[len(nums) // 2]

        # method2
        majority, count = None, 0

        for num in nums:
            if count == 0:
                majority = num

            count += 1 if num == majority else -1

        return majority

        # # method3
        # hash_map = {}
        # majority = None
        # count = 0

        # for n in nums:
        #     hash_map[n] = 1 + hash_map.get(n, 0)

        #     if hash_map[n] > count:
        #         majority = n
        #         count = hash_map[n]

        # return majority
