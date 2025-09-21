class Solution:
    def trailingZeroes(self, n: int) -> int:
        # # method1
        # fac = 1

        # while n != 0:
        #     fac *= n
        #     n -= 1

        # count = 0
        # while fac != 0 and fac % 10 == 0:
        #     count += 1
        #     fac //= 10

        # return count

        # method2
        count = 0

        while n > 0:
            n //= 5
            count += n

        return count
