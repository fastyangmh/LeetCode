class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x

            r = prefix % k

            ans += count.get(r, 0)

            count[r] = count.get(r, 0) + 1

        return ans
