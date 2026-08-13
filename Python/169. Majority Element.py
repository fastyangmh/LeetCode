class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0

        for n in nums:
            ans = n if count == 0 else ans
            count += 1 if n == ans else -1

        return ans
