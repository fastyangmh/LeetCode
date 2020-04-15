class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda n: not len(str(n)) % 2, nums)))


if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]
    print(Solution().findNumbers(nums))
    nums = [555, 901, 482, 1771]
    print(Solution().findNumbers(nums))
