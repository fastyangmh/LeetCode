class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s) - 1):
            a, b = int(s[i]), int(s[i + 1])

            if abs(a - b) > 2:
                return False

        return True
