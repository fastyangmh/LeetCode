class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        read = write = 1

        while read < n:
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

            read += 1

        return write
