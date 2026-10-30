class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            if s[i] == s[(i + 1) % n]:
                total += 1

        if k == total - 1:
            return total

        if k == total:
            return n - total

        return 0
