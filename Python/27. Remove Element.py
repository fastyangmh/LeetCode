class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for x in nums:
            if x != val:
                nums[write] = x
                write += 1

        return write
