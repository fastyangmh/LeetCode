from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # method1
        # counter = {}

        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1

        # return sorted(counter, key=lambda x: counter[x])[-k:]

        # # method2
        # freq = Counter(nums)
        # heap = [(-count, num) for num, count in freq.items()]
        # heapq.heapify(heap)
        # rets = []

        # for _ in range(k):
        #     count, num = heapq.heappop(heap)
        #     rets.append(num)

        # return rets

        # method3
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        rets = []

        for num, count in freq.items():
            bucket[count].append(num)

        for count in range(len(bucket) - 1, -1, -1):
            for num in bucket[count]:
                rets.append(num)
                if len(rets) == k:
                    return rets
