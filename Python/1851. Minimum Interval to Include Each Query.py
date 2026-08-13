import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(intervals), len(queries)

        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        ans = [-1] * n
        min_heap = []
        j = 0

        for q, i in sorted_queries:
            while j < m and intervals[j][0] <= q:
                left, right = intervals[j]

                heapq.heappush(min_heap, (right - left + 1, right))

                j += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                ans[i] = min_heap[0][0]

        return ans
