class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        sum_first = sum_second = 0
        first_min = second_min = float("inf")

        for row in units:
            first = second = float("inf")

            for x in row:
                if x < first:
                    second = first
                    first = x
                elif x < second:
                    second = x

            if len(row) == 1:
                second = 0

            sum_first += first
            sum_second += second

            first_min = min(first_min, first)
            second_min = min(second_min, second)

        return max(sum_first, first_min + sum_second - second_min)
