class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        ans = 0

        for p in prices:
            ans = max(ans, p - buy)
            buy = min(buy, p)

        return ans
