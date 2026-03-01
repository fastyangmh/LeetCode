class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        factorials = [1] * 10

        for idx in range(1, 10):
            factorials[idx] = factorials[idx - 1] * idx

        total = sum(factorials[int(ch)] for ch in str(n))

        return sorted(str(total)) == sorted(str(n))
