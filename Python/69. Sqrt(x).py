class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x

        while left < right:
            mid = (left + right + 1) // 2
            square = mid * mid

            if square <= x:
                left = mid
            else:
                right = mid - 1

        return left
