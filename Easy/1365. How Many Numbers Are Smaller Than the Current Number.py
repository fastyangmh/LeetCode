class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for n in nums:
            count.append(sorted(list(nums)).index(n))
        return count


if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]
    print(Solution().smallerNumbersThanCurrent(nums))
    nums = [6, 5, 4, 8]
    print(Solution().smallerNumbersThanCurrent(nums))
    nums = [7, 7, 7, 7]
    print(Solution().smallerNumbersThanCurrent(nums))
