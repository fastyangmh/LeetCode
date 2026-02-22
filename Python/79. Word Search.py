class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # # method1
        # rows = len(board)
        # cols = len(board[0])

        # def backtrack(ri, ci, idx):
        #     if idx == len(word):
        #         return True
        #     if not (0 <= ri < rows and 0 <= ci < cols and board[ri][ci] == word[idx]):
        #         return False

        #     tmp, board[ri][ci] = board[ri][ci], "_"

        #     found = (
        #         backtrack(ri + 1, ci, idx + 1)
        #         or backtrack(ri - 1, ci, idx + 1)
        #         or backtrack(ri, ci + 1, idx + 1)
        #         or backtrack(ri, ci - 1, idx + 1)
        #     )

        #     board[ri][ci] = tmp

        #     return found

        # for ri in range(rows):
        #     for ci in range(cols):
        #         if board[ri][ci] != word[0]:
        #             continue
        #         found = backtrack(ri, ci, 0)
        #         if found:
        #             return found

        # return False

        # method2
        rows, cols = len(board), len(board[0])

        def dfs(ri, ci, word_idx):
            if board[ri][ci] != word[word_idx]:
                return False

            if word_idx == len(word) - 1:
                return True

            tmp = board[ri][ci]
            board[ri][ci] = "_"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = ri + dr, ci + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if dfs(nr, nc, word_idx + 1):
                    return True

            board[ri][ci] = tmp

            return False

        for ri in range(rows):
            for ci in range(cols):
                if dfs(ri, ci, 0):
                    return True

        return False
