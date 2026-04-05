from collections import deque


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

        return dp[-1] if dp[-1] != float("inf") else -1

        # method2
        # if amount == 0:
        #     return 0

        # queue = deque([0])
        # seen = set([0])
        # count = 0

        # while queue:
        #     count += 1

        #     for _ in range(len(queue)):
        #         curr = queue.popleft()

        #         for coin in coins:
        #             nxt = coin + curr

        #             if nxt == amount:
        #                 return count
        #             elif nxt > amount:
        #                 continue
        #             elif nxt not in seen:
        #                 seen.add(nxt)
        #                 queue.append(nxt)

        # return -1
