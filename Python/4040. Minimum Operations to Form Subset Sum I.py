class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        INF = float("inf")

        dp = [INF] * (sum + 1)
        dp[0] = 0

        for x in nums:
            options = {}

            value = x
            cost = 0

            while value <= sum:
                options[value] = min(options.get(value, INF), cost)

                value *= 2
                cost += 1

            value = x
            cost = 0

            while value > 0:
                options[value] = min(options.get(value, INF), cost)

                value //= 2
                cost += 1

            ndp = dp[:]

            for value, cost in options.items():
                for s in range(sum - value + 1):
                    ndp[s + value] = min(ndp[s + value], dp[s] + cost)

            dp = ndp

        return dp[-1] if dp[-1] != INF else -1
