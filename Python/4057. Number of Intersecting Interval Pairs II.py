import heapq


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        heap = []
        ans = 0

        for start, end in intervals:
            while heap and heap[0] < start:
                heapq.heappop(heap)

            ans += len(heap)

            heapq.heappush(heap, end)

        return ans
