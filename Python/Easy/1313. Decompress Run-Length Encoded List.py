class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for idx in range(0, len(nums), 2):
            l += [nums[idx+1]]*nums[idx]
        return l


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().decompressRLElist(nums))
    nums = [1, 1, 2, 3]
    print(Solution().decompressRLElist(nums))
