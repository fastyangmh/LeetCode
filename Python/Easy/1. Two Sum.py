# import
from typing import List


# class
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        ret = []

        for i, num in enumerate(nums):
            diff = target - num
            j = hash_map.get(diff)

            if j is not None:
                ret += [j, i]
                break

            hash_map[num] = i

        return ret


if __name__ == "__main__":
    # Example 1:
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1], Solution().twoSum(nums, target)

    # Example 2:
    nums = [3, 2, 4]
    target = 6
    assert Solution().twoSum(nums, target) == [1, 2], Solution().twoSum(nums, target)

    # Example 3:
    nums = [3, 3]
    target = 6
    assert Solution().twoSum(nums, target) == [0, 1], Solution().twoSum(nums, target)
