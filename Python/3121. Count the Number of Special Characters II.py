class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)

        last_lower = [-1] * 26
        first_upper = [n] * 26

        for i, char in enumerate(word):
            if char.islower():
                j = ord(char) - ord("a")
                last_lower[j] = i
            else:
                j = ord(char) - ord("A")
                first_upper[j] = min(first_upper[j], i)

        return sum(l < u for l, u in zip(last_lower, first_upper) if l >= 0 and u < n)
