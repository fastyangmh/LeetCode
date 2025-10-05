from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # method1
        # low, high = 1, len(nums) - 1

        # while low < high:
        #     mid = (low + high) // 2

        #     count = sum(num <= mid for num in nums)

        #     if count > mid:
        #         high = mid
        #     else:
        #         low = mid + 1

        # return low

        # method2
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
