class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        # # method1
        # nl = l ** (1 / k)
        # nl = int(nl) if nl.is_integer() else int(nl + 1)

        # nr = int(r ** (1 / k) + 1)

        # return nr - nl

        # method2
        a = int(l ** (1 / k))

        while a**k < l:
            a += 1

        while a > 0 and (a - 1) ** k >= l:
            a -= 1

        b = int(r ** (1 / k))

        while (b + 1) ** k <= r:
            b += 1

        while b**k > r:
            b -= 1

        return b - a + 1
