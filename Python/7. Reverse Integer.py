class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1

        sign = 1 if x > 0 else -1
        x = abs(x)
        y = 0

        while x > 0:
            digit = x % 10
            x //= 10

            if y > (INT_MAX - digit) // 10:
                return 0

            y = y * 10 + digit

        return y * sign
