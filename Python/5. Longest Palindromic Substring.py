class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # method1
        # def expand(l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1

        #     return l + 1, r - 1

        # start = end = 0

        # for i in range(len(s)):
        #     l1, r1 = expand(i, i)
        #     l2, r2 = expand(i, i + 1)

        #     if r1 - l1 > end - start:
        #         end, start = r1, l1
        #     if r2 - l2 > end - start:
        #         end, start = r2, l2

        # return s[start : end + 1]

        # method2
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        start = 0
        max_len = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i + 1][j - 1])

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start : start + max_len]
