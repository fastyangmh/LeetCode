class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            node = root

            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(ri, ci, node):
            curr_chr = board[ri][ci]

            if curr_chr not in node.children:
                return

            curr_node = node.children[curr_chr]

            if curr_node.word is not None:
                res.append(curr_node.word)
                curr_node.word = None

            if not curr_node.children:
                node.children.pop(curr_chr)
                return

            board[ri][ci] = "_"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = ri + dr, ci + dc

                if not (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "_"):
                    continue

                dfs(nr, nc, curr_node)

            board[ri][ci] = curr_chr

        for ri in range(rows):
            for ci in range(cols):
                dfs(ri, ci, root)

        return res
