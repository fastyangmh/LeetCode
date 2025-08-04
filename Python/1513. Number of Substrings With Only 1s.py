class Solution:
    def numSub(self, s: str) -> int:
        MODULO = 10**9 + 7
        ans = 0
        count = 0

        for c in s:
            if c == "1":
                count += 1
                ans += count
            else:
                count = 0

        return ans % MODULO
