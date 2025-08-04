class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hash_table = {}
        for idx in range(lo, hi+1):
            hash_table[idx] = self.power(integer=idx)
        return sorted(hash_table.items(), key=lambda x: x[1])[k-1][0]

    def power(self, integer):
        count = 0
        while integer != 1:
            if integer % 2 == 0:
                integer = integer//2
            else:
                integer = 3*integer+1
            count += 1
        return count


if __name__ == '__main__':
    # ex1    ans 13
    lo = 12
    hi = 15
    k = 2
    print(Solution().getKth(lo=lo, hi=hi, k=k))

    # ex2    ans 1
    lo = 1
    hi = 1
    k = 1
    print(Solution().getKth(lo=lo, hi=hi, k=k))

    # ex3    ans 7
    lo = 7
    hi = 11
    k = 4
    print(Solution().getKth(lo=lo, hi=hi, k=k))

    # ex4    ans 13
    lo = 10
    hi = 20
    k = 5
    print(Solution().getKth(lo=lo, hi=hi, k=k))

    # ex5    ans 570
    lo = 1
    hi = 1000
    k = 777
    print(Solution().getKth(lo=lo, hi=hi, k=k))
