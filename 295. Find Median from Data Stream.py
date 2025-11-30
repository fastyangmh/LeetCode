import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        top = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, top)

        if len(self.min_heap) > len(self.max_heap):
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])

        return (-self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
