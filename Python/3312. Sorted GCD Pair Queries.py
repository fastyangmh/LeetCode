from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        cnt = [0] * (mx + 1)

        for x in nums:
            cnt[x] += 1

        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            divisible = 0
            for multiple in range(g, mx + 1, g):
                divisible += cnt[multiple]

            pairs = divisible * (divisible - 1) // 2

            for multiple in range(g * 2, mx + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        prefix = [0] * (mx + 1)

        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        return [bisect_right(prefix, q) for q in queries]
