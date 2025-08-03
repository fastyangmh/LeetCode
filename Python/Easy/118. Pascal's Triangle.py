from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return self.generate(numRows - 1) + [[1, 1]]

        results = self.generate(numRows - 1)

        last_ret = results[-1]
        cur_ret = [1] * numRows

        for idx in range(1, numRows - 1):
            cur_ret[idx] = last_ret[idx - 1] + last_ret[idx]
        results.append(cur_ret)

        return results
