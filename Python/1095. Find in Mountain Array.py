# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        n = mountainArr.length()

        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if mountainArr.get(m) >= mountainArr.get(m + 1):
                r = m
            else:
                l = m + 1

        peak_idx = l

        l, r = 0, peak_idx

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value == target:
                return m
            elif value < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak_idx + 1, n - 1

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value == target:
                return m
            elif value < target:
                r = m - 1
            else:
                l = m + 1

        return -1
