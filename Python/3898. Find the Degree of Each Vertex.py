class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(v) for v in matrix]
