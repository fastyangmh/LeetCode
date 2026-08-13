class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[-1])
        ans = 1
        prev_end = points[0][-1]

        for idx in range(1, len(points)):
            start, end = points[idx]

            if prev_end < start:
                prev_end = end
                ans += 1

        return ans
