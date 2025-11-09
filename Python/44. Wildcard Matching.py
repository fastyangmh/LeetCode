class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # method1
        # m, n = len(s), len(p)
        # prev = [False] * (n + 1)
        # prev[0] = True

        # for j in range(1, n + 1):
        #     if p[j - 1] == "*":
        #         prev[j] = prev[j - 1]

        # for i in range(1, m + 1):
        #     curr = [False] * (n + 1)

        #     for j in range(1, n + 1):
        #         if p[j - 1] == "*":
        #             curr[j] = curr[j - 1] or prev[j]
        #         elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
        #             curr[j] = prev[j - 1]

        #     prev = curr

        # return prev[-1]

        # method2
        i = j = 0
        star_idx = match_idx = -1

        while i < len(s):
            if j < len(p) and (p[j] == "?" or p[j] == s[i]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star_idx = j
                match_idx = i
                j += 1
            elif star_idx != -1:
                j = star_idx + 1
                match_idx += 1
                i = match_idx
            else:
                return False

        while j < len(p) and p[j] == "*":
            j += 1

        return j == len(p)
