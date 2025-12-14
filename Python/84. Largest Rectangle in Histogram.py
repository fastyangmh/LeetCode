class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()
                height = heights[mid]

                right = i
                left = stack[-1] if stack else -1
                width = right - left - 1

                max_area = max(max_area, width * height)

            stack.append(i)

        return max_area
