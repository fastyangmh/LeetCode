from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # method1
        # freq = Counter(nums)
        # heap = []

        # for num, count in freq.items():
        #     heapq.heappush(heap, (count, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [v[1] for v in heap]

        # method2
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num, count in freq.items():
            bucket[count].append(num)

        for count in range(len(bucket) - 1, -1, -1):
            for num in bucket[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans
