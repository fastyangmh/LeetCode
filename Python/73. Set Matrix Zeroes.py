from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # method1
        # rows, cols = len(matrix), len(matrix[0])

        # zero_row_indices = set()
        # zero_col_indices = set()

        # for ri in range(rows):
        #     if 0 not in matrix[ri]:
        #         continue

        #     zero_row_indices.add(ri)

        #     for ci in range(cols):
        #         if matrix[ri][ci] == 0:
        #             zero_col_indices.add(ci)

        # for ri in range(rows):
        #     if ri in zero_row_indices:
        #         matrix[ri] = [0] * cols

        #     for ci in zero_col_indices:
        #         matrix[ri][ci] = 0

        # method2
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][ci] == 0 for ci in range(cols))
        first_col_zero = any(matrix[ri][0] == 0 for ri in range(rows))

        for ri in range(1, rows):
            for ci in range(1, cols):
                if matrix[ri][ci] == 0:
                    matrix[0][ci] = 0
                    matrix[ri][0] = 0

        for ri in range(1, rows):
            for ci in range(1, cols):
                if matrix[0][ci] == 0 or matrix[ri][0] == 0:
                    matrix[ri][ci] = 0

        if first_row_zero:
            for ci in range(cols):
                matrix[0][ci] = 0

        if first_col_zero:
            for ri in range(rows):
                matrix[ri][0] = 0
