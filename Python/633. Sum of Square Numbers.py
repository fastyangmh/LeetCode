class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)

        while left <= right:
            s = left**2 + right**2

            if s == c:
                return True
            if s < c:
                left += 1
            else:
                right -= 1

        return False
