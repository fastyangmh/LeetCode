from collections import Counter
from math import factorial


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        middle = ""
        half = [0] * 26

        for i in range(26):
            ch = chr(ord("a") + i)

            if cnt[ch] % 2 == 1:
                middle = ch

            half[i] = cnt[ch] // 2

        n = sum(half)

        def count_permutations(counts, length):
            ways = factorial(length)

            for x in counts:
                ways //= factorial(x)

            return ways

        total_ways = count_permutations(half, n)

        if total_ways < k:
            return ""

        left = []

        while n > 0:
            for i in range(26):
                if half[i] == 0:
                    continue

                ways = total_ways * half[i] // n

                if k > ways:
                    k -= ways
                else:
                    left.append(chr(ord("a") + i))
                    half[i] -= 1
                    n -= 1
                    total_ways = ways
                    break

        left = "".join(left)

        return left + middle + left[::-1]
