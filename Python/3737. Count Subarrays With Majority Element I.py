class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            score = 0

            for r in range(l, n):
                if nums[r] == target:
                    score += 1
                else:
                    score -= 1

                if score > 0:
                    ans += 1

        return ans
