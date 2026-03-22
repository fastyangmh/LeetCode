from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # # method1
        # rows, cols = len(board), len(board[0])

        # def dfs(r, c):
        #     if not (0 <= r < rows and 0 <= c < cols and board[r][c] == "O"):
        #         return

        #     board[r][c] = "#"

        #     dfs(r + 1, c)
        #     dfs(r - 1, c)
        #     dfs(r, c + 1)
        #     dfs(r, c - 1)

        # for r in range(rows):
        #     dfs(r, 0)
        #     dfs(r, cols - 1)

        # for c in range(cols):
        #     dfs(0, c)
        #     dfs(rows - 1, c)

        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] != "#":
        #             board[r][c] = "X"
        #         else:
        #             board[r][c] = "O"

        # method2
        rows, cols = len(board), len(board[0])

        def bfs(starts):
            for r, c in starts:
                board[r][c] = "#"

            queue = deque(starts)

            while queue:
                r, c = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O"):
                        continue

                    board[nr][nc] = "#"
                    queue.append((nr, nc))

        starts = []

        for r in range(rows):
            if board[r][0] == "O":
                starts.append((r, 0))
            if board[r][cols - 1] == "O":
                starts.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == "O":
                starts.append((0, c))
            if board[rows - 1][c] == "O":
                starts.append((rows - 1, c))

        bfs(starts)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "#":
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"
