class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        second = 0
        cx, cy = points[0]
        for x, y in points[1:]:
            second += max(abs(x-cx), abs(y-cy))
            cx, cy = x, y
        return second


if __name__ == "__main__":
    points = [[1, 1], [3, 4], [-1, 0]]
    print(Solution().minTimeToVisitAllPoints(points))
    points = [[3, 2], [-2, 2]]
    print(Solution().minTimeToVisitAllPoints(points))
