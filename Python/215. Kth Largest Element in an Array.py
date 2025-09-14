from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # method1
        # return sorted(nums)[-k]

        # method2
        import heapq

        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
