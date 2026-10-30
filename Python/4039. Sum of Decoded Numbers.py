class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0

        for num in nums:
            width = num % 10
            d = str(num // 10)

            x = int(d[:width])
            y = int(d[width:])

            ans = (ans + pow(x, y, MOD)) % MOD

        return ans
