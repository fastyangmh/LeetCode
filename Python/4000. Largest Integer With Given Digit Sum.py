class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0
        elif s > 9 * n:
            return -1

        digits = []
        remaining = s

        for _ in range(n):
            d = min(9, remaining)
            digits.append(str(d))
            remaining -= d

        return int("".join(digits))
