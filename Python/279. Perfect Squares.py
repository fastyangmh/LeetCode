from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        # method1
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[-1]

        # # method2
        # squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        # visited = set([n])
        # queue = deque([n])
        # level = 0

        # while queue:
        #     level += 1

        #     for _ in range(len(queue)):
        #         remainder = queue.popleft()

        #         for sq in squares:
        #             next_val = remainder - sq

        #             if next_val == 0:
        #                 return level

        #             if next_val < 0:
        #                 break

        #             if next_val not in visited:
        #                 queue.append(next_val)
        #                 visited.add(next_val)

        # return level
