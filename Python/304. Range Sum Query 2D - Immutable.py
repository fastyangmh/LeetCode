class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                top = prefix[r - 1][c]
                left = prefix[r][c - 1]
                top_left = prefix[r - 1][c - 1]
                curr = matrix[r - 1][c - 1]

                prefix[r][c] = top + left - top_left + curr

        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2 + 1][col2 + 1]
        top = self.prefix[row1][col2 + 1]
        left = self.prefix[row2 + 1][col1]
        top_left = self.prefix[row1][col1]

        return total - top - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
