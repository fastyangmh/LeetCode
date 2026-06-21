class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0

        for x in range(max(1, n - k), n + k + 1):
            ans += x if n & x == 0 else 0

        return ans
