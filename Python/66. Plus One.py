class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            d = digits[i]

            total = carry + d

            digits[i] = total % 10
            carry = total // 10

        if carry != 0:
            return [carry] + digits
        return digits
