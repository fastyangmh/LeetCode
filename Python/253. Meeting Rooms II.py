import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # # method1
        # starts = sorted([v[0] for v in intervals])
        # ends = sorted([v[1] for v in intervals])

        # rooms = ans = 0
        # start_idx = end_idx = 0

        # while start_idx < len(intervals):
        #     if starts[start_idx] < ends[end_idx]:
        #         rooms += 1
        #         ans = max(ans, rooms)
        #         start_idx += 1
        #     else:
        #         rooms -= 1
        #         end_idx += 1

        # return ans

        # method2
        intervals.sort()
        max_rooms = 0
        heap = []

        for start, end in intervals:
            while heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

            max_rooms = max(max_rooms, len(heap))

        return max_rooms
