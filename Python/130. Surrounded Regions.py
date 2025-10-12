class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # # method1 mine
        # m, n = len(board), len(board[0])
        # directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # paths = set()

        # def handler(y, x):
        #     if board[y][x] == "X" or (y, x) in paths:
        #         return
        #     paths.add((y, x))

        #     for dy, dx in directions:
        #         if not 0 <= x + dx < n or not 0 <= y + dy < m:
        #             continue

        #         handler(y + dy, x + dx)

        # for y in range(m):
        #     for x in range(n):
        #         handler(y, x)

        #         if not any(
        #             y_ == 0 or y_ == m - 1 or x_ == 0 or x_ == n - 1 for y_, x_ in paths
        #         ):
        #             for y_, x_ in paths:
        #                 board[y_][x_] = "X"

        #         paths = set()

        # method2
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return

            board[r][c] = "#"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
