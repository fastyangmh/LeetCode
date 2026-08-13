class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        n = len(digits)

        pivot = n - 2

        while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
            pivot -= 1

        if pivot < 0:
            return -1

        successor = n - 1

        while successor >= 0 and digits[successor] <= digits[pivot]:
            successor -= 1

        digits[pivot], digits[successor] = digits[successor], digits[pivot]

        left, right = pivot + 1, n - 1

        while left < right:
            digits[left], digits[right] = digits[right], digits[left]

            left += 1
            right -= 1

        ret = 0
        INT_MAX = 2**31 - 1

        for i in range(n):
            d = int(digits[i])

            if ret > (INT_MAX - d) // 10:
                return -1

            ret = ret * 10 + d

        return ret
