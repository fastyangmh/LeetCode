from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # method1
        # N = 9
        # n = 3

        # rows = [set() for _ in range(N)]
        # cols = [set() for _ in range(N)]
        # boxes = [set() for _ in range(N)]

        # for r in range(N):
        #     for c in range(N):
        #         cell = board[r][c]

        #         if cell == ".":
        #             continue

        #         box_id = (r // n) * n + (c // n)

        #         if cell in rows[r] or cell in cols[c] or cell in boxes[box_id]:
        #             return False

        #         rows[r].add(cell)
        #         cols[c].add(cell)
        #         boxes[box_id].add(cell)

        # return True

        # method2
        N = 9
        n = int(N**0.5)

        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                v = board[r][c]

                if v == ".":
                    continue

                b = (r // n) * n + (c // n)

                d = ord(v) - ord("1")
                bit = 1 << d

                if rows[r] & bit or cols[c] & bit or boxes[b] & bit:
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

        return True
