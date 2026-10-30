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
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for v, cnt in counter.items():
            bucket[cnt].append(v)

        ans = []

        for cnt in range(len(bucket) - 1, -1, -1):
            for v in bucket[cnt]:
                ans.append(v)

                if len(ans) == k:
                    return ans

        return ans
