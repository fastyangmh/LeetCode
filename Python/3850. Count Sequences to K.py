from fractions import Fraction
from collections import Counter


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        dp = Counter({Fraction(1, 1): 1})

        for num in nums:
            newdp = Counter()

            for val, cnt in dp.items():
                newdp[val * num] += cnt
                newdp[val / num] += cnt
                newdp[val] += cnt

            dp = newdp

        return dp[Fraction(k, 1)]
