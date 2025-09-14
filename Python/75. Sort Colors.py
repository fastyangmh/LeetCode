class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # method1
        # count0 = count1 = count2 = 0

        # for n in nums:
        #     if n == 0:
        #         count0 += 1
        #     elif n == 1:
        #         count1 += 1
        #     else:
        #         count2 += 1

        # for idx in range(count0):
        #     nums[idx] = 0

        # for idx in range(count0, count0 + count1):
        #     nums[idx] = 1

        # for idx in range(count0 + count1, count0 + count1 + count2):
        #     nums[idx] = 2

        # method2
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
