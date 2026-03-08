class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = len(grid)

        for bit in range(17, -1, -1):
            temp = [[] for _ in range(rows)]
            possible = True

            for idx in range(rows):
                for num in grid[idx]:
                    if num & (1 << bit) == 0:
                        temp[idx].append(num)

                if not temp[idx]:
                    possible = False
                    break

            if not possible:
                ans |= 1 << bit
            else:
                grid = temp

        return ans
