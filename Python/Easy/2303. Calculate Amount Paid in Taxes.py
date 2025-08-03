from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        last_upper = 0

        for upper, percent in brackets:
            percent /= 100
            tax = min(income, upper) - last_upper
            taxes += tax * percent
            last_upper = upper

            if upper > income:
                break

        return taxes
