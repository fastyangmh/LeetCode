class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            day_used = 1
            curr = 0

            for weight in weights:
                if curr + weight > capacity:
                    day_used += 1
                    curr = weight
                else:
                    curr += weight

            return day_used <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
