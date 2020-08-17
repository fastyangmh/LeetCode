class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            if grid[x][0] < 0:
                count += (m-x)*n
                break
            for y in range(n):
                if grid[x][y] < 0:
                    count += n-y
                    break
        return count


if __name__ == "__main__":
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(Solution().countNegatives(grid))
    grid = [[3, 2], [1, 0]]
    print(Solution().countNegatives(grid))
    grid = [[1, -1], [-1, -1]]
    print(Solution().countNegatives(grid))
    grid = [[-1]]
    print(Solution().countNegatives(grid))
