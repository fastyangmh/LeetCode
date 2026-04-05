class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                return l
            l += 1
            r -= 1
        return -1
