class Solution:
    def filterOccupiedIntervals(
        self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int
    ) -> List[List[int]]:
        occupiedIntervals.sort()
        merged = []

        for s, e in occupiedIntervals:
            if merged and s <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])

        ans = []

        for l, r in merged:
            if l < freeStart:
                left_end = min(r, freeStart - 1)

                if l <= left_end:
                    ans.append([l, left_end])

            if r > freeEnd:
                right_start = max(l, freeEnd + 1)

                if right_start <= r:
                    ans.append([right_start, r])

        return ans
