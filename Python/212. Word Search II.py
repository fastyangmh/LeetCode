class Trie:
    def __init__(self):
        self.data = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for w in words:
            node = root

            for c in w:
                if c not in node.data:
                    node.data[c] = Trie()
                node = node.data[c]

            node.word = w

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(ri, ci, node):
            curr_chr = board[ri][ci]

            if curr_chr not in node.data:
                return

            curr_node = node.data[curr_chr]

            if curr_node.word is not None:
                res.append(curr_node.word)
                curr_node.word = None

            if not curr_node.data:
                node.data.pop(curr_chr)
                return

            board[ri][ci] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = ri + dr, ci + dc

                if not (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#"):
                    continue

                dfs(nr, nc, curr_node)

            board[ri][ci] = curr_chr

        for ri in range(rows):
            for ci in range(cols):
                dfs(ri, ci, root)

        return res
