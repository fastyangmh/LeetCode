class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for st, ed in intervals:
            if merged and st <= merged[-1][-1]:
                merged[-1][-1] = max(merged[-1][-1], ed)
            else:
                merged.append([st, ed])

        return merged
