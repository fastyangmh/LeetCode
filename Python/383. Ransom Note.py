class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for c in magazine:
            i = ord(c) - ord("a")
            count[i] += 1

        for c in ransomNote:
            i = ord(c) - ord("a")

            count[i] -= 1

            if count[i] < 0:
                return False

        return True
