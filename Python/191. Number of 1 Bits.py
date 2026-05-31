class Solution:
    def hammingWeight(self, n: int) -> int:
        # # method1
        # ans = 0

        # while n:
        #     ans += n & 1
        #     n >>= 1

        # return ans

        # method2
        ans = 0

        while n:
            ans += 1
            n &= n - 1

        return ans
