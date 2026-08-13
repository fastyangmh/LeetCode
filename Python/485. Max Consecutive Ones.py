class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0

        for num in nums:
            count = count + 1 if num == 1 else 0
            ans = max(ans, count)
        return ans
