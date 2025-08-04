class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = 0
        n += symbols[s[-1]]
        last = n
        for idx in range(len(s)-2, -1, -1):
            if symbols[s[idx]] < last:
                n -= symbols[s[idx]]
            else:
                n += symbols[s[idx]]
            last = symbols[s[idx]]
        return n


if __name__ == "__main__":
    x = 'MCMXCIV'
    print(Solution().romanToInt(x))
