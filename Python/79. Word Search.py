class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(ri, ci, idx):
            if idx == len(word):
                return True
            if not (0 <= ri < rows and 0 <= ci < cols and board[ri][ci] == word[idx]):
                return False

            tmp, board[ri][ci] = board[ri][ci], "_"

            found = (
                backtrack(ri + 1, ci, idx + 1)
                or backtrack(ri - 1, ci, idx + 1)
                or backtrack(ri, ci + 1, idx + 1)
                or backtrack(ri, ci - 1, idx + 1)
            )

            board[ri][ci] = tmp

            return found

        for ri in range(rows):
            for ci in range(cols):
                if board[ri][ci] != word[0]:
                    continue
                found = backtrack(ri, ci, 0)
                if found:
                    return found

        return False