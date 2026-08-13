class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ans = 0
        stack = []

        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] > x:
                h = heights[stack.pop()]

                right = i - 1
                left = stack[-1] + 1 if stack else 0
                w = right - left + 1

                ans = max(ans, h * w)
            stack.append(i)

        return ans
