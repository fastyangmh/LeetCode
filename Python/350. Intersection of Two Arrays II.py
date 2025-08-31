from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # map_ = {}
        # rets = []

        # for n in nums1:
        #     map_.setdefault(n, 0)
        #     map_[n] += 1

        # for n in nums2:
        #     if map_.get(n, 0) > 0:
        #         rets.append(n)
        #         map_[n] -= 1

        # return rets

        nums1.sort()
        nums2.sort()
        rets = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                rets.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return rets
