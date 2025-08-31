class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # # method1
        # if n < 1:
        #     return False

        # while n % 3 == 0:
        #     n //= 3

        # return n == 1

        # # method2
        # if n == 1:
        #     return True
        # if n < 1 or n % 3 != 0:
        #     return False

        # return self.isPowerOfThree(n // 3)

        # method3
        return n > 0 and 3**19 % n == 0
