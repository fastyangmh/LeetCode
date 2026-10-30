class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            takes = 0

            for p in piles:
                takes += (p + k - 1) // k

            return takes <= h

        l, r = 1, max(piles)

        while l < r:
            k = (l + r) // 2

            if check(k):
                r = k
            else:
                l = k + 1

        return l
