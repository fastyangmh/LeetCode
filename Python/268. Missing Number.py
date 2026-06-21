class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # method1
        # n = len(nums)
        # expected = n * (n + 1) // 2
        # actual = sum(nums)

        # return expected - actual

        # method2
        ans = len(nums)

        for i, n in enumerate(nums):
            ans ^= i ^ n

        return ans

        # # method3
        # ans = len(nums)

        # for i, n in enumerate(nums):
        #     ans += i - n

        # return ans
