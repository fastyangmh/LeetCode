class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2

        total = sum(nums)
        first = sum(nums[:half])

        ans = 0

        for i in range(n):
            if 2 * first > total:
                ans += 1

            outgoing = nums[i]
            incoming = nums[(i + half) % n]

            first += incoming - outgoing

        return ans
