class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def first_digit(v):
            while v >= 10:
                v //= 10
            return v

        ans = 0

        for l in range(n):
            for r in range(l, n):
                s = prefix[r + 1] - prefix[l]

                if s % 10 != x:
                    continue

                if first_digit(s) == x:
                    ans += 1

        return ans
