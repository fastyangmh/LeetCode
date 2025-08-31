from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        if numRows == 1:
            return res

        for idx in range(1, numRows):
            prev = res[idx - 1]
            l = len(prev)
            curr = [1] + [prev[i] + prev[i + 1] for i in range(l - 1)] + [1]
            res.append(curr)
        return res
