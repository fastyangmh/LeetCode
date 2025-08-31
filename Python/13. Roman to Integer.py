class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        l = len(s)

        for idx in range(l - 1, -1, -1):
            sign = 1
            if idx < l - 1:
                sign = 1 if value_map[s[idx]] >= value_map[s[idx + 1]] else -1
            ans += sign * value_map[s[idx]]

        return ans
