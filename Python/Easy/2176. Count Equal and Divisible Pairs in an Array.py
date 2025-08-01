# import
from typing import List


# class
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        equal_maps: dict[int, list] = {}
        ret = 0

        for j, vj in enumerate(nums):
            pairs_indices = equal_maps.get(vj)

            if pairs_indices is None:
                equal_maps[vj] = [j]
                continue

            for i in pairs_indices:
                if i < j and (i * j) % k == 0:
                    ret += 1

            pairs_indices.append(j)

        return ret


if __name__ == "__main__":
    # Example 1:
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
    assert Solution().countPairs(nums, k) == 4, Solution().countPairs(nums, k)

    # Example 2:

    nums = [1, 2, 3, 4]
    k = 1
    assert Solution().countPairs(nums, k) == 0, Solution().countPairs(nums, k)
