from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # method1
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for curr in range(1, amount + 1):
            for coin in coins:
                if curr < coin:
                    continue

                dp[curr] = min(dp[curr], dp[curr - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1

        # # method2
        # if amount == 0:
        #     return 0

        # visited = set([0])
        # queue = [(0, 0)]

        # while queue:
        #     curr, steps = queue.pop(0)

        #     for coin in coins:
        #         nxt = curr + coin
        #         if nxt == amount:
        #             return steps + 1

        #         if nxt < amount and nxt not in visited:
        #             visited.add(nxt)
        #             queue.append((nxt, steps + 1))

        # return -1
