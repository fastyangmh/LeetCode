class Solution:
    def mySqrt(self, x: int) -> int:
        # # method1, find the last False; False, False, True, True, True
        # l, r = 0, x + 1

        # while l < r:
        #     m = (l + r) // 2
        #     s = m * m

        #     if s > x:
        #         r = m
        #     else:
        #         l = m + 1

        # return l - 1

        # method2, find the last True; True, True, True, False, False
        l, r = 0, x

        while l < r:
            m = (l + r + 1) // 2
            s = m * m

            if s <= x:
                l = m
            else:
                r = m - 1

        return l
