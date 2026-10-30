import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []

        for _, height in envelopes:
            i = bisect.bisect_left(tails, height)

            if i == len(tails):
                tails.append(height)
            else:
                tails[i] = height

        return len(tails)
