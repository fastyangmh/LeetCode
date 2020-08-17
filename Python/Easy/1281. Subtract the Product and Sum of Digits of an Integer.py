class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        for c in str(n):
            s += int(c)
            p *= int(c)
        return p-s


if __name__ == "__main__":
    n = 234
    print(Solution().subtractProductAndSum(n))
    n = 4421
    print(Solution().subtractProductAndSum(n))
