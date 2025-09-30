class Solution:
    def mySqrt(self, x: int) -> int:
        # # method1
        # i = 0

        # while i * i <= x:
        #     i += 1

        # return i - 1

        # method2
        if x < 2:
            return x

        l, r = 1, x // 2

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square < x:
                l = mid + 1
            elif square > x:
                r = mid - 1
            else:
                return mid

        return r

        # # method3
        # res = x

        # while res * res > x:
        #     res = (res + x // res) // 2

        # return res

        # # method4 is similar to method2
        # if x < 2:
        #     return x

        # count = 0
        # temp = x

        # while temp > 0:
        #     count += 1
        #     temp >>= 1

        # res = 0

        # for i in range((count + 1) // 2, -1, -1):
        #     res |= 1 << i
        #     if res * res > x:
        #         res ^= 1 << i

        # return res
