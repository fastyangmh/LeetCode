from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        counter = {}
        result = 0

        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                counter[s] = 1 + counter.get(s, 0)

        for n3 in nums3:
            for n4 in nums4:
                s = n3 + n4
                result += counter.get(-s, 0)

        return result
