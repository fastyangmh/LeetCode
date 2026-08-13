class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        prev = 0
        ans = 0

        for i in range(n - 1, -1, -1):
            curr = symbols[s[i]]

            if prev > curr:
                ans -= curr
            else:
                ans += curr

            prev = curr

        return ans
