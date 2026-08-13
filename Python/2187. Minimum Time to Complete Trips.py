class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(limit):
            return sum(limit // v for v in time) >= totalTrips

        left, right = 1, min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
