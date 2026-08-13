class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[write] = nums2[j]
                j -= 1
            else:
                nums1[write] = nums1[i]
                i -= 1

            write -= 1
