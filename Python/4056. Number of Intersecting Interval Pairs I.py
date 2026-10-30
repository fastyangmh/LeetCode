class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                start_i, end_i = intervals[i]
                start_j, end_j = intervals[j]

                if max(start_i, start_j) <= min(end_i, end_j):
                    ans += 1

        return ans
