from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # method1
        # N = 9
        # n = int(N**0.5)
        # rows = [set() for _ in range(N)]
        # cols = [set() for _ in range(N)]
        # boxes = [set() for _ in range(N)]

        # for r in range(N):
        #     for c in range(N):
        #         v = board[r][c]

        #         if v == ".":
        #             continue

        #         b = (r // n) * n + (c // n)

        #         if v in rows[r] or v in cols[c] or v in boxes[b]:
        #             return False

        #         rows[r].add(v)
        #         cols[c].add(v)
        #         boxes[b].add(v)

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

        # # method3
        # def check_repeat(s):
        #     map_ = {}
        #     for c in s:
        #         if not c.isdigit():
        #             continue

        #         map_.setdefault(c, 0)

        #         if map_[c] > 0:
        #             return True
        #         map_[c] += 1
        #     return False

        # for row in board:
        #     is_repeat = check_repeat(row)

        #     if is_repeat:
        #         return False

        # for col in zip(*board):
        #     is_repeat = check_repeat(list(col))

        #     if is_repeat:
        #         return False

        # for col_idx in range(0, len(board), 3):
        #     for row_idx in range(0, len(board), 3):
        #         boxes = []
        #         row = board[row_idx : row_idx + 3]

        #         for i in range(3):
        #             boxes += row[i][col_idx : col_idx + 3]

        #         is_repeat = check_repeat(boxes)

        #         if is_repeat:
        #             return False

        # return True
