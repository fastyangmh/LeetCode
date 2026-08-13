class Solution:
    def sumAndMultiply(self, n: int) -> int:
        backward = 0

        while n:
            d = n % 10
            n //= 10

            if d != 0:
                backward = backward * 10 + d

        forward = 0
        s = 0

        while backward:
            d = backward % 10
            backward //= 10

            s += d
            forward = forward * 10 + d

        return forward * s
