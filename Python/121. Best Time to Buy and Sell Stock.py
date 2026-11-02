class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - buy)
            buy = min(buy, prices[i])

        return ans
