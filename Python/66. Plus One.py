from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # carry = 1
        # for idx in range(len(digits) - 1, -1, -1):
        #     digits[idx] += carry
        #     carry = digits[idx] // 10
        #     digits[idx] %= 10

        #     if carry == 0:
        #         break
        # if carry != 0:
        #     digits = [carry] + digits
        # return digits

        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] + 1 < 10:
                digits[idx] += 1
                return digits

            digits[idx] = 0

            if idx == 0:
                return [1] + digits
