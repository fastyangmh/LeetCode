class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        k %= rows * cols
        if k == 0:
            return grid

        new_grid = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                new_idx = (idx + k) % (rows * cols)

                nr = new_idx // cols
                nc = new_idx % cols

                new_grid[nr][nc] = grid[r][c]

        return new_grid
