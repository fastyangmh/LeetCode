class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            e = 0

            for p in piles:
                e += (p + k - 1) // k

            return e <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
