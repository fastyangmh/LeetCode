class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        max_val = max(nums)
        spf = list(range(max_val + 1))

        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = []

            while x > 1:
                p = spf[x]
                factors.append(p)

                while x % p == 0:
                    x //= p

            return factors

        factors = [get_factors(x) for x in nums]
        prime_count = [0] * (max_val + 1)
        ans = 0
        left = 0
        distinct = 0

        for right in range(len(nums)):
            for p in factors[right]:
                if prime_count[p] == 0:
                    distinct += 1
                prime_count[p] += 1

            while distinct > k:
                for p in factors[left]:
                    prime_count[p] -= 1

                    if prime_count[p] == 0:
                        distinct -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
