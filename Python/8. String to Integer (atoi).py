class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        i = 0
        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] in {"+", "-"}:
            sign = 1 if s[i] == "+" else -1
            i += 1

        limit = INT_MAX if sign == 1 else -INT_MIN

        ans = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if ans > (limit - digit) // 10:
                return sign * limit

            ans = ans * 10 + digit

            i += 1

        return sign * ans
