from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def vertical_flip(m):
            u, d = 0, len(m) - 1

            while u < d:
                m[u], m[d] = m[d], m[u]
                u += 1
                d -= 1

        def transpose(m):
            for ri in range(len(m)):
                for ci in range(ri + 1, len(m)):
                    m[ri][ci], m[ci][ri] = m[ci][ri], m[ri][ci]

        vertical_flip(matrix)
        transpose(matrix)
