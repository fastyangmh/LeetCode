class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        temp = {
            1: [["."]],
            2: [["..", ".."]],
            3: [["..", "..", ".."], ["...", "..."]],
            4: [["..", "..", "..", ".."], ["....", "...."], ["..#", "...", "#.."]],
        }

        for t in temp[k]:
            r, c = len(t), len(t[0])

            if r > m or c > n:
                continue

            res = [["#"] * n for _ in range(m)]

            for i in range(r):
                for j in range(c):
                    res[i][j] = t[i][j]

            for i in range(r, m):
                res[i][c - 1] = "."

            for j in range(c, n):
                res[m - 1][j] = "."

            return ["".join(row) for row in res]

        return []
