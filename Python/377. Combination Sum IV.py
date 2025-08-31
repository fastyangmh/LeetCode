from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for idx in range(1, len(dp)):
            for n in nums:
                if n <= idx:
                    dp[idx] += dp[idx - n]

        return dp[target]
