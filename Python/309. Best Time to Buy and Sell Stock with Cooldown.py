class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # method1
        # n = len(prices)

        # hold = [0] * n
        # sold = [0] * n
        # rest = [0] * n

        # hold[0] = rest[0] - prices[0]

        # for i in range(1, n):
        #     hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        #     sold[i] = hold[i - 1] + prices[i]
        #     rest[i] = max(rest[i - 1], sold[i - 1])

        # return max(rest[-1], sold[-1])

        # method2
        n = len(prices)

        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, n):
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
