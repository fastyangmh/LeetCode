import math


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                g = math.gcd(a, b)

                ans = max(ans, (a * b) // (g**2))

        return ans
