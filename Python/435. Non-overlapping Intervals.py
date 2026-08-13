class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])
        ans = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if prev_end > start:
                ans += 1
            else:
                prev_end = end

        return ans
