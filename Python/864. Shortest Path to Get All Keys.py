from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        target = 0
        start_r = start_c = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    start_r, start_c = r, c
                elif grid[r][c].islower():
                    target |= 1 << (ord(grid[r][c]) - ord("a"))

        queue = deque([(start_r, start_c, 0)])
        visited = {queue[0]}
        dist = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            for _ in range(len(queue)):
                r, c, keys = queue.popleft()

                if keys == target:
                    return dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#"):
                        continue

                    ch = grid[nr][nc]

                    if "A" <= ch <= "F":
                        required = 1 << (ord(ch) - ord("A"))
                        if keys & required == 0:
                            continue

                    new_keys = keys

                    if "a" <= ch <= "f":
                        new_keys |= 1 << (ord(ch) - ord("a"))

                    state = (nr, nc, new_keys)
                    if state in visited:
                        continue
                    visited.add(state)
                    queue.append(state)

            dist += 1

        return -1
