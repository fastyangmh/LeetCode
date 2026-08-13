class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def check(day):
            bouquets = 0
            cnt = 0

            for x in bloomDay:
                if day >= x:
                    cnt += 1
                    if cnt == k:
                        bouquets += 1
                        cnt = 0
                else:
                    cnt = 0

            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
