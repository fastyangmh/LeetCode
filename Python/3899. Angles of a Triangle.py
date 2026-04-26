import math


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides

        if a + b <= c or a + c <= b or b + c <= a:
            return []

        def cal_angle(a, b, c):
            return round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))), 5)

        return sorted(
            [
                cal_angle(a, b, c),
                cal_angle(b, c, a),
                cal_angle(a, c, b),
            ]
        )
