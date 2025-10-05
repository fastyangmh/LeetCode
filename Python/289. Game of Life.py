from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def handler(y, x):
            directions = (
                (1, 0),
                (-1, 0),
                (0, -1),
                (0, 1),
                (-1, -1),
                (1, 1),
                (1, -1),
                (-1, 1),
            )
            live_neighbors = 0
            is_alive = 1 if abs(board[y][x]) == 1 else 0

            for dx, dy in directions:
                if not 0 <= y + dy < m or not 0 <= x + dx < n:
                    continue

                live_neighbors += 1 if abs(board[y + dy][x + dx]) == 1 else 0

            if is_alive == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[y][x] = -1
            else:
                if live_neighbors == 3:
                    board[y][x] = 2

        for y in range(m):
            for x in range(n):
                handler(y, x)

        for y in range(m):
            for x in range(n):
                board[y][x] = 1 if board[y][x] > 0 else 0
