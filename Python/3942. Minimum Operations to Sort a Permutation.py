class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(nums, f):
            dec = 0

            for i in range(1, n):
                if nums[i] < nums[i - 1]:
                    if dec != 0 or nums[-1] > nums[0]:
                        return float("inf")

                    dec = i

            return min(dec, (n - dec) % n) if f else min(dec, (n - dec) % n + 2)

        ans = min(solve(nums, False), solve(nums[::-1], True) + 1)

        return -1 if ans == float("inf") else ans
