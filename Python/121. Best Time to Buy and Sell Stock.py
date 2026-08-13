class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0

        for p in prices:
            profit = max(profit, p - buy)
            buy = min(buy, p)

        return profit
