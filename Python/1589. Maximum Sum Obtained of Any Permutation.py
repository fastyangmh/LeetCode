class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7

        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1

        for i in range(1, n):
            diff[i] += diff[i - 1]

        count = diff[:n]

        count.sort()
        nums.sort()
        ans = 0

        for a, b in zip(nums, count):
            ans = (ans + a * b) % MOD

        return ans
