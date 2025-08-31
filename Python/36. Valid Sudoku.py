from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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

        l = len(board)
        rows = [set() for _ in range(l)]
        cols = [set() for _ in range(l)]
        boxes = [set() for _ in range(l)]

        for ri in range(l):
            for ci in range(l):
                ch = board[ri][ci]

                if ch == ".":
                    continue

                bi = (ri // 3) * 3 + (ci // 3)

                if ch in rows[ri] or ch in cols[ci] or ch in boxes[bi]:
                    return False

                rows[ri].add(ch)
                cols[ci].add(ch)
                boxes[bi].add(ch)

        return True
