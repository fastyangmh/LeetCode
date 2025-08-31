class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        count = 0

        while diff:
            count += 1
            diff &= diff - 1

        return count
