import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # method1
        heap = []

        for x, y in points:
            d = x**2 + y**2
            heapq.heappush(heap, (-d, (x, y)))

            if len(heap) > k:
                heapq.heappop(heap)

        return [v[1] for v in heap]

        # # method2
        # return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
