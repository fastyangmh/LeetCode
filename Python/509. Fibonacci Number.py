class Solution:
    def fib(self, n: int) -> int:
        # # method1
        # mem = {0: 0, 1: 1}

        # def f(n):
        #     if n not in mem:
        #         mem[n]=f(n-1)+f(n-2)
        #     return mem[n]

        # return f(n)

        # method2
        if n < 2:
            return n

        a, b = 0, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b