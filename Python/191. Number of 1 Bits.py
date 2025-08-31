class Solution:
    def hammingWeight(self, n: int) -> int:
        # # method1
        # return bin(n)[2:].count("1")

        # # method2
        # count = 0

        # while n:
        #     count += n & 1
        #     n >>= 1

        # return count

        # method3
        count = 0

        while n:
            count += 1
            n &= n - 1

        return count
