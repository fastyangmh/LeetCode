class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26

        for char in word:
            if char.islower():
                idx = ord(char) - ord("a")
                lower[idx] = True
            else:
                idx = ord(char) - ord("A")
                upper[idx] = True

        return sum(lower[idx] * upper[idx] for idx in range(26))
