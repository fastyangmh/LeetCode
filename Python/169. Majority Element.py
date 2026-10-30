class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        cnt = 0

        for x in nums:
            ans = ans if cnt > 0 else x
            cnt += 1 if x == ans else -1

        return ans
