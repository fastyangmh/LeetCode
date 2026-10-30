class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        prefix = 1

        for x in nums:
            ans.append(prefix)
            prefix *= x

        suffix = 1

        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
