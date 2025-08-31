class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0

        for l, r in zip(s[:-1], s[1:]):
            if l.lower() != r.lower():
                count += 1

        return count
