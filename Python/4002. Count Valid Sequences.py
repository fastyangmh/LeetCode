class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            if a < 0 or b > a:
                return 0

            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        total = comb(n - 1, k - 1)

        if (n - k) % 2 != 0:
            return total

        m = (n - k) // 2

        odd = comb(m + k - 1, k - 1)

        return (total - odd) % MOD
