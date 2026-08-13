class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largest_rectangle(heights: list[int]) -> int:
            heights.append(0)
            stack = []
            ret = 0

            for i, x in enumerate(heights):
                while stack and heights[stack[-1]] > x:
                    h = heights[stack.pop()]

                    right = i - 1
                    left = stack[-1] + 1 if stack else 0
                    w = right - left + 1

                    ret = max(ret, h * w)

                stack.append(i)
            heights.pop()
            return ret

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0

            ans = max(ans, largest_rectangle(heights))

        return ans
