import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append([left, -height])
            events.append([right, height])

        events.sort()

        results = []
        max_heap = [0]
        prev_max = 0
        removed = {}

        for x, h in events:
            if h < 0:
                heapq.heappush(max_heap, h)
            else:
                removed[-h] = removed.get(-h, 0) + 1

            while max_heap and removed.get(max_heap[0], 0):
                removed[max_heap[0]] -= 1
                heapq.heappop(max_heap)

            curr_max = -max_heap[0]

            if curr_max != prev_max:
                results.append([x, curr_max])
                prev_max = curr_max

        return results
