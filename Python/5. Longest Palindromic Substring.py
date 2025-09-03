class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # method1
        # def expand(l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return s[l + 1 : r]  # slicing is left-inclusive and right-exclusive

        # res = ""

        # for i in range(len(s)):
        #     odd = expand(i, i)
        #     even = expand(i, i + 1)

        #     res = max(res, odd, even, key=len)

        # return res

        # method2
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (
                r - l - 1
            )  # it's similar method1. [l+1, r-1] -> (r-1) - (l+1) +1 -> r - l - 1

        start = end = 0

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]
