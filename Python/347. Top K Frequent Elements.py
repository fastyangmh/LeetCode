class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # method1
        # freq = {}

        # for n in nums:
        #     freq[n] = freq.get(n, 0) + 1

        # return sorted(freq, key=lambda key: freq[key])[-k:]

        # method2
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for n, count in freq.items():
            bucket[count].append(n)

        res = []

        for count in range(len(bucket) - 1, -1, -1):
            for n in bucket[count]:
                res.append(n)

                if len(res) == k:
                    return res
