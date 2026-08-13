class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # # method1 time: O(mn), space: O(mn)
        # rows, cols = len(matrix), len(matrix[0])
        # side = 0
        # dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # for r in range(1, rows + 1):
        #     for c in range(1, cols + 1):
        #         if matrix[r - 1][c - 1] != "1":
        #             continue

        #         upper = dp[r - 1][c]
        #         left = dp[r][c - 1]
        #         upper_left = dp[r - 1][c - 1]

        #         dp[r][c] = min(upper, left, upper_left) + 1

        #         side = max(side, dp[r][c])

        # return side * side

        # method2, time: O(mn), space: O(n)
        rows, cols = len(matrix), len(matrix[0])
        side = 0

        dp = [0] * (cols + 1)

        for r in range(1, rows + 1):
            prev = dp[0]

            for c in range(1, cols + 1):
                tmp = dp[c]

                if matrix[r - 1][c - 1] == "0":
                    dp[c] = 0
                else:
                    upper = dp[c]
                    left = dp[c - 1]
                    upper_left = prev

                    dp[c] = min(upper, left, upper_left) + 1

                    side = max(side, dp[c])

                prev = tmp

        return side * side
