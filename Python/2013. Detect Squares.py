from collections import Counter, defaultdict


class DetectSquares:
    def __init__(self):
        self.points = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        ways = 0

        for y2, y2_cnt in self.points[qx].items():
            if y2 == qy:
                continue

            side = abs(y2 - qy)

            for x2 in (qx - side, qx + side):
                ways += y2_cnt * self.points[x2][y2] * self.points[x2][qy]

        return ways


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
