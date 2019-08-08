class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for idx, n in enumerate(nums):
                if target < n:
                    return idx
            return idx+1


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))
