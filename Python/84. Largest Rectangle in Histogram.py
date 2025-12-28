class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()
                mid_h = heights[mid]

                left = i - 1
                right = stack[-1] if stack else -1
                w = left - right

                max_area = max(max_area, mid_h * w)

            stack.append(i)

        return max_area
