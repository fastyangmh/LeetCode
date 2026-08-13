class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1 = hold2 = -prices[0]
        release1 = release2 = 0

        for i in range(1, len(prices)):
            p = prices[i]

            hold1 = max(hold1, -p)
            release1 = max(release1, hold1 + p)

            hold2 = max(hold2, release1 - p)
            release2 = max(release2, hold2 + p)

        return release2
