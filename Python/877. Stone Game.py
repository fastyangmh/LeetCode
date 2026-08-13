class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # method1
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                pick_left = piles[left] - dp[left + 1][right]
                pick_right = piles[right] - dp[left][right - 1]

                dp[left][right] = max(pick_left, pick_right)

        return dp[0][n - 1] > 0

        # # method2
        # # This greedy strategy is valid because:
        # # 1. The number of piles is even, allowing Alice to choose either all even-indexed
        # # piles or all odd-indexed piles.
        # # 2. Players can only take from the two ends, so Alice can stick to her chosen parity.
        # # 3. The total number of stones is odd, ensuring the sums of the even-indexed and
        # # odd-indexed piles cannot be equal.
        # # 4. Alice moves first, so she gets to choose which parity to commit to.
        # return True
