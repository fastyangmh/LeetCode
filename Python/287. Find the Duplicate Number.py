class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # # method1
        # l, r = 1, len(nums) - 1

        # while l < r:
        #     m = (l + r) // 2

        #     if sum(n <= m for n in nums) > m:
        #         r = m
        #     else:
        #         l = m + 1

        # return l

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
