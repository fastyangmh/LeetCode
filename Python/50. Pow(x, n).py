class Solution:
    def myPow(self, x: float, n: int) -> float:
        # # method1
        # if n == 0:
        #     return 1

        # if n < 0:
        #     x = 1 / x
        #     n = abs(n)

        # half = self.myPow(x, n // 2)
        # half *= half

        # if n % 2 == 0:
        #     return half
        # else:
        #     return x * half

        # method2
        if n < 0:
            x = 1 / x
            n = abs(n)

        res = 1

        while n > 0:
            if n & 1:
                res *= x

            n //= 2
            x *= x

        return res
