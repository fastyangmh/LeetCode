class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n2 = n >> 1
        while n:
            if (n ^ n2) & 1 == 0:
                return False
            n >>= 1
            n2 >>= 1
        return True


if __name__ == '__main__':
    # ex1    ans    True
    n = 5
    print(Solution().hasAlternatingBits(n=n))

    # ex2    ans    False
    n = 7
    print(Solution().hasAlternatingBits(n=n))

    # ex3    ans    False
    n = 11
    print(Solution().hasAlternatingBits(n=n))

    # ex4    ans    True
    n = 10
    print(Solution().hasAlternatingBits(n=n))

    # ex5    ans    False
    n = 3
    print(Solution().hasAlternatingBits(n=n))
