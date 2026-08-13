class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                top = prefix[r - 1][c]
                left = prefix[r][c - 1]
                top_left = prefix[r - 1][c - 1]
                curr = mat[r - 1][c - 1]

                prefix[r][c] = top + left - top_left + curr

        ans = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                row1, col1 = max(0, r - k), max(0, c - k)
                row2, col2 = min(rows - 1, r + k), min(cols - 1, c + k)

                total = prefix[row2 + 1][col2 + 1]
                top = prefix[row1][col2 + 1]
                left = prefix[row2 + 1][col1]
                top_left = prefix[row1][col1]

                ans[r][c] = total - top - left + top_left

        return ans
