from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # # method1
        # rows, cols = len(heights), len(heights[0])

        # def dfs(r, c, visited):
        #     visited.add((r, c))

        #     for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        #         nr, nc = r + dr, c + dc

        #         if not (
        #             0 <= nr < rows
        #             and 0 <= nc < cols
        #             and (nr, nc) not in visited
        #             and heights[nr][nc] >= heights[r][c]
        #         ):
        #             continue

        #         dfs(nr, nc, visited)

        # pacific = set()
        # atlantic = set()

        # for r in range(rows):
        #     dfs(r, 0, pacific)
        #     dfs(r, cols - 1, atlantic)

        # for c in range(cols):
        #     dfs(0, c, pacific)
        #     dfs(rows - 1, c, atlantic)

        # return [list(v) for v in pacific & atlantic]

        # method2
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if not (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))

            return visited

        pacific_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic_starts = [(r, cols - 1) for r in range(rows)] + [
            (rows - 1, c) for c in range(cols)
        ]

        return [list(v) for v in bfs(pacific_starts) & bfs(atlantic_starts)]
