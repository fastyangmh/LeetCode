class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend < 0) == (divisor < 0) else -1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            multiplier, div = 1, divisor

            while dividend >= (div << 1):
                div <<= 1
                multiplier <<= 1
            dividend -= div
            quotient += multiplier

        if (quotient * sign) >= 2**31:
            return 2**31 - 1

        return quotient * sign
