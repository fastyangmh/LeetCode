class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        idx = len(s) - 1

        while idx >= 0 and s[idx] in vowels:
            idx -= 1

        return s[: idx + 1]
