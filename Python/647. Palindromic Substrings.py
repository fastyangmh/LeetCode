class Solution:
    def countSubstrings(self, s: str) -> int:
        # # method1
        # def expand(l, r):
        #     count = 0

        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         count += 1
        #         l -= 1
        #         r += 1

        #     return count

        # ans = 0

        # for i in range(len(s)):
        #     ans += expand(i, i)
        #     ans += expand(i, i + 1)

        # return ans

        # method2
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        count = 0

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])

                count += 1 if dp[i][j] else 0

        return count
