class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = float("inf")
        l = 0
        curr = 0

        for r, n in enumerate(nums):
            curr += n

            while curr >= target:
                ans = min(ans, r - l + 1)
                curr -= nums[l]
                l += 1

        return ans if ans != float("inf") else 0
