class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return l, r

        result = 1

        for i in range(n):

            for l0, r0 in ((i, i), (i, i + 1)):
                l, r = expand(l0, r0)
                result = max(result, r - l)

                l1, r1 = expand(l - 1, r)
                result = max(result, r1 - l1 - 1)

                l2, r2 = expand(l, r + 1)
                result = max(result, r2 - l2 - 1)

                if result >= n:
                    return n

        return result
