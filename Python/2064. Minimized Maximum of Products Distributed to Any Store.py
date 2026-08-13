class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(amount):
            stores = 0

            for q in quantities:
                stores += (q + amount - 1) // amount

            return stores <= n

        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
