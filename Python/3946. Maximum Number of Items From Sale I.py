class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        factors = [x[0] for x in items]
        prices = [x[1] for x in items]
        bonus = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and factors[j] % factors[i] == 0:
                    bonus[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            cost = prices[i]
            gain = 1 + bonus[i]

            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + gain)

        for i in range(n):
            cost = prices[i]

            for b in range(cost, budget + 1):
                dp[b] = max(dp[b], dp[b - cost] + 1)

        return dp[-1]
