class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, m

        while l <= r:
            part1 = (l + r) // 2
            part2 = (m + n + 1) // 2 - part1

            max_left1 = nums1[part1 - 1] if part1 > 0 else float("-inf")
            max_left2 = nums2[part2 - 1] if part2 > 0 else float("-inf")

            min_right1 = nums1[part1] if part1 < m else float("inf")
            min_right2 = nums2[part2] if part2 < n else float("inf")

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) & 1:
                    return max(max_left1, max_left2)
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                r = part1 - 1
            else:
                l = part1 + 1
