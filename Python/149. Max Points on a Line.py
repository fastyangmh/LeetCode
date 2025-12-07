from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 1

        for i in range(n):
            x1, y1 = points[i]
            slopes = {}
            same = 0
            max_count = 0

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx, dy = x2 - x1, y2 - y1

                if dx == 0 and dy == 0:
                    same += 1
                    continue

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1

                slope = (dx, dy)
                slopes[slope] = slopes.get(slope, 0) + 1
                max_count = max(max_count, slopes[slope])

            res = max(res, max_count + same + 1)

        return res
