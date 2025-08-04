from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix):
            return 0
        row, col = len(matrix), len(matrix[0])
        max_area = self.largestRectangleArea(
            heights=[int(v) for v in matrix[0]])
        for r in range(row):
            temp = []
            for c in range(col):
                if r+1 != row:
                    temp.append((int(matrix[r][c])+1)*int(matrix[r+1][c]))
                else:
                    temp.append(int(matrix[r][c]))
            if r+1 != row:
                matrix[r+1] = temp
            area = self.largestRectangleArea(heights=temp)
            max_area = area if area > max_area else max_area
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not len(heights):
            return 0
        max_area = 0
        stack = [0]
        indices = [0]
        heights += [0]
        for idx, v in enumerate(heights):
            temp = 0
            idx += 1
            if v >= stack[-1]:
                stack.append(v)
                indices.append(idx)
            else:
                while v < stack[-1]:
                    temp = stack[-1]*(idx-indices[-2]-1)
                    max_area = temp if temp > max_area else max_area
                    stack.pop()
                    indices.pop()
                stack.append(v)
                indices.append(idx)
        return max_area


if __name__ == "__main__":
    Input = [["1", "0", "1", "0", "0"],
             ["1", "0", "1", "1", "1"],
             ["1", "1", "1", "1", "1"],
             ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(Input))
    Input = [["1"]]
    print(Solution().maximalRectangle(Input))
    Input = [["1", "0", "1", "1", "1", "1", "0", "1", "1"],
             ["0", "1", "0", "1", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "1", "0", "1", "1", "0"],
             ["1", "1", "1", "0", "1", "0", "1", "0", "1"]]
    print(Solution().maximalRectangle(Input))
