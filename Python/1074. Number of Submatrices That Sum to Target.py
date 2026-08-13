class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        for top in range(rows):
            col_sum = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    col_sum[col] += matrix[bottom][col]

                count = {0: 1}
                prefix = 0

                for x in col_sum:
                    prefix += x
                    ans += count.get(prefix - target, 0)
                    count[prefix] = count.get(prefix, 0) + 1

        return ans
