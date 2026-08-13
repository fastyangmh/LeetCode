class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += count.get(prefix - k, 0)
            count[prefix] = count.get(prefix, 0) + 1

        return ans
