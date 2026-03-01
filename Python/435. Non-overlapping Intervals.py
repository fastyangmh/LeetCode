class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = float("-inf")
        remove = 0

        for start, end in intervals:
            if prev_end > start:
                remove += 1
            else:
                prev_end = end

        return remove
