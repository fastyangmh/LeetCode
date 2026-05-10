class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])

        left, right = min(n, r), max(n, r)

        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right**0.5 + 1)):
            if not is_prime[i]:
                continue

            for j in range(i * i, right + 1, i):
                is_prime[j] = False

        return sum(i for i in range(left, right + 1) if is_prime[i])
