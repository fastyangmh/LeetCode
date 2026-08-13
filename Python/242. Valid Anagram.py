class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for c in s:
            i = ord(c) - ord("a")
            count[i] += 1

        for c in t:
            i = ord(c) - ord("a")
            count[i] -= 1

            if count[i] < 0:
                return False

        return True
