class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # method1 time: O(D), space: O(D)
        travel_days = set(days)
        last_day = days[-1]

        dp = [0] * (last_day + 1)

        for d in range(1, last_day + 1):
            if d not in travel_days:
                dp[d] = dp[d - 1]
            else:
                cost1 = dp[d - 1] + costs[0]
                cost2 = dp[max(0, d - 7)] + costs[1]
                cost3 = dp[max(0, d - 30)] + costs[2]

                dp[d] = min(cost1, cost2, cost3)

        return dp[-1]

        # # method2 time: O(n**2), space: O(n)
        # n = len(days)
        # memo = [-1] * n

        # def dfs(i):
        #     if i >= n:
        #         return 0

        #     if memo[i] != -1:
        #         return memo[i]

        #     j = i

        #     while j < n and days[j] < days[i] + 1:
        #         j += 1

        #     cost1 = costs[0] + dfs(j)

        #     j = i

        #     while j < n and days[j] < days[i] + 7:
        #         j += 1

        #     cost2 = costs[1] + dfs(j)

        #     j = i

        #     while j < n and days[j] < days[i] + 30:
        #         j += 1

        #     cost3 = costs[2] + dfs(j)

        #     memo[i] = min(cost1, cost2, cost3)

        #     return memo[i]

        # return dfs(0)
