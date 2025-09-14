from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # method1 (upper right corner)
        # rows, cols = len(matrix), len(matrix[0])
        # ri, ci = 0, cols - 1

        # while ri < rows and ci >= 0:
        #     if matrix[ri][ci] < target:
        #         ri += 1
        #     elif matrix[ri][ci] > target:
        #         ci -= 1
        #     else:
        #         return True

        # return False

        # method2 (from lower left corner)
        rows, cols = len(matrix), len(matrix[0])
        ri, ci = rows - 1, 0

        while ri >= 0 and ci < cols:
            if matrix[ri][ci] > target:
                ri -= 1
            elif matrix[ri][ci] < target:
                ci += 1
            else:
                return True
        return False
