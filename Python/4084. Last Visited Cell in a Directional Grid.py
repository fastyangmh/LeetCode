class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

        visited = set()
        r = c = 0

        while (r, c) not in visited:
            visited.add((r, c))
            dr, dc = directions[grid[r][c]]
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                break

            r, c = nr, nc

        return [r, c]
