class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[idx] <= s[idx + 1] for idx in range(len(s) - 1)):
            return 0

        if len(s) == 2:
            return -1

        min_char, max_char = min(s[1:-1]), max(s[1:-1])

        if s[0] <= s[-1] and (min_char >= s[0] or max_char <= s[-1]):
            return 1

        return 3 if s[-1] < min_char and s[0] > max_char else 2
