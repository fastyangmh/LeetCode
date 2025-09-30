class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp, multiple = b, 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            quotient += multiple

        quotient *= sign

        if quotient > 2**31 - 1:
            return 2**31 - 1
        elif quotient < -(2**31):
            return -(2**31)
        else:
            return quotient
