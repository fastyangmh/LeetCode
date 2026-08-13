class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            repaired = 0

            for r in ranks:
                n = int((time / r) ** 0.5)
                repaired += n

            return repaired >= cars

        left, right = 1, min(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
