class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1

        MOD = 1337

        def myPow(a, k):
            a %= MOD
            ret = 1

            while k > 0:
                if k & 1:
                    ret *= a
                a = (a * a) % MOD
                k >>= 1

            return ret

        last = b.pop()

        part1 = myPow(self.superPow(a, b), 10)
        part2 = myPow(a, last)

        return (part1 * part2) % MOD
