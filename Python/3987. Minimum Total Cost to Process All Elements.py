class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        res = k          # current resources
        ops = 0          # operations already performed
        ans = 0

        for x in nums:
            if res < x:
                need = x - res
                m = (need + k - 1) // k

                ans = (ans + m * (2 * ops + m + 1) // 2) % MOD
                ops += m
                res += m * k

            res -= x

        return ans % MODou