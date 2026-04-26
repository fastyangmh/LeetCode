class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 0

        for n in arr:
            dp[n] = dp.get(n - difference, 0) + 1
            ans = max(ans, dp[n])

        return ans
