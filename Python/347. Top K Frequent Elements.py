from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # method1
        # count = Counter(nums)
        # heap = []

        # for num, count in count.items():
        #     heapq.heappush(heap, (count, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [v[1] for v in heap]

        # method2
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            bucket[cnt].append(num)

        ans = []

        for cnt in range(len(bucket) - 1, -1, -1):
            for num in bucket[cnt]:
                ans.append(num)

                if len(ans) == k:
                    return ans
