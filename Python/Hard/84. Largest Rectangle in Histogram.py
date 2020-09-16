from typing import List


class Solution:
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
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights=heights))
