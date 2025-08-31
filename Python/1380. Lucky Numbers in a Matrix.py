from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        map_ = {}

        for row in matrix:
            min_num = min(row)
            col_idx = row.index(min_num)

            if col_idx not in map_:
                map_[col_idx] = [min_num]
            else:
                map_[col_idx].append(min_num)

        for col_idx, min_nums in map_.items():
            col = [row[col_idx] for row in matrix]
            max_num = max(col + min_nums)

            if max_num in min_nums:
                return [max_num]

        return []
