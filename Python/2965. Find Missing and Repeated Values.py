from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        map_ = {}
        missing_number = -1
        repeated_number = -1

        for g in grid:
            for e in g:
                if e in map_:
                    repeated_number = e
                else:
                    map_[e] = 1

        for idx in range(1, len(map_) + 1):
            if idx not in map_:
                missing_number = idx

        if missing_number == -1:
            missing_number = len(map_) + 1

        return [repeated_number, missing_number]
