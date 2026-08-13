class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            scores = 0
            dp[i] = float("-inf")

            for take in range(3):
                if i + take >= n:
                    break

                scores += stoneValue[i + take]

                dp[i] = max(dp[i], scores - dp[i + take + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
