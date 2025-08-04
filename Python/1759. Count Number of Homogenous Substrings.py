class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        left = 0

        for right in range(len(s)):
            if s[left] == s[right]:
                res += right - left + 1
            else:
                res += 1
                left = right

        return res % MOD
