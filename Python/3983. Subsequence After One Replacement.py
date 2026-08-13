class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n = len(s)

        dp0 = 0
        dp1 = -1

        for c in t:
            old0, old1 = dp0, dp1

            if old0 < n and s[old0] == c:
                dp0 = old0 + 1

            if old0 < n:
                dp1 = max(dp1, old0 + 1)

            if old1 >= 0 and old1 < n and s[old1] == c:
                dp1 = max(dp1, old1 + 1)

            if old0 == n or old1 == n:
                return True

        return dp0 == n or dp1 == n
