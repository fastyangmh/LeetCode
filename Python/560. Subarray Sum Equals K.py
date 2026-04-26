class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = pfx = 0
        pfx_count = {0: 1}

        for n in nums:
            pfx += n
            ans += pfx_count.get(pfx - k, 0)
            pfx_count[pfx] = pfx_count.get(pfx, 0) + 1

        return ans
