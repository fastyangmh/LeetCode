class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # method1
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if (
                not 0 <= x + dx < cols
                or not 0 <= y + dy < rows
                or matrix[y + dy][x + dx] == "."
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res

        # # method2
        # top, bottom = 0, len(matrix) - 1
        # left, right = 0, len(matrix[0]) - 1
        # res = []

        # while top <= bottom and left <= right:
        #     for j in range(left, right + 1):
        #         res.append(matrix[top][j])
        #     top += 1

        #     for i in range(top, bottom + 1):
        #         res.append(matrix[i][right])
        #     right -= 1

        #     if top <= bottom:
        #         for j in range(right, left - 1, -1):
        #             res.append(matrix[bottom][j])
        #         bottom -= 1

        #     if left <= right:
        #         for i in range(bottom, top - 1, -1):
        #             res.append(matrix[i][left])
        #         left += 1

        # return res
