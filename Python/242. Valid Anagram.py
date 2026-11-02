class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = [0] * 26

        for c in s:
            chars[ord(c) - ord("a")] += 1

        for c in t:
            idx = ord(c) - ord("a")

            chars[idx] -= 1

            if chars[idx] < 0:
                return False

        return True
