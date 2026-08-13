class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # method1
        rows, cols = len(matrix), len(matrix[0])
        x, y = 0, 0
        dx, dy = 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not (
                0 <= x + dx < cols
                and 0 <= y + dy < rows
                and matrix[y + dy][x + dx] != "."
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res

        # # method2
        # top, bottom = 0, len(matrix) - 1
        # left, right = 0, len(matrix[0]) - 1
        # ans = []

        # while top <= bottom and left <= right:
        #     for j in range(left, right + 1):
        #         ans.append(matrix[top][j])
        #     top += 1

        #     for i in range(top, bottom + 1):
        #         ans.append(matrix[i][right])
        #     right -= 1

        #     if top <= bottom:
        #         for j in range(right, left - 1, -1):
        #             ans.append(matrix[bottom][j])
        #         bottom -= 1

        #     if left <= right:
        #         for i in range(bottom, top - 1, -1):
        #             ans.append(matrix[i][left])
        #         left += 1

        # return ans
