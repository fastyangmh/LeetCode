class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        idx = 0
        l = len(s)
        signed = 1
        ans = 0
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        # rule1
        while idx < l and s[idx] == " ":
            idx += 1

        if idx == l:
            return 0

        # rule2
        if s[idx] == "-":
            signed = -1
            idx += 1
        elif s[idx] == "+":
            signed = 1
            idx += 1

        # rule3
        while idx < l and s[idx].isdigit():
            ans = (ans * 10) + int(s[idx])
            idx += 1

        # rule4
        ans *= signed

        if ans < INT_MIN:
            ans = INT_MIN
        elif ans > INT_MAX:
            ans = INT_MAX

        return ans
