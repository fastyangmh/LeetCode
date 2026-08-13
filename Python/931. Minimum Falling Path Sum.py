class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # method1 time: O(n**2), space: O(n)
        n = len(matrix)

        curr = matrix[0][:]

        for r in range(1, n):
            prev = curr[:]
            for c in range(n):
                best = prev[c]

                if c > 0:
                    best = min(best, prev[c - 1])

                if c < n - 1:
                    best = min(best, prev[c + 1])

                curr[c] = matrix[r][c] + best

        return min(curr)

        # # method2 time: O(n**2), space: O(n**2)
        # n = len(matrix)
        # directions = ((1, -1), (1, 0), (1, 1))
        # dist = [[float("inf")] * n for _ in range(n)]

        # for c in range(n):
        #     dist[0][c] = matrix[0][c]

        # for r in range(n):
        #     for c in range(n):
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc

        #             if not (0 <= nr < n and 0 <= nc < n):
        #                 continue

        #             dist[nr][nc] = min(dist[nr][nc], dist[r][c] + matrix[nr][nc])

        # return min(dist[-1][c] for c in range(n))
