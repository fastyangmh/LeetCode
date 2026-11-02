class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []

        prefix = 1

        for num in nums:
            ans.append(prefix)
            prefix *= num

        suffix = 1

        for idx in range(len(nums) - 1, -1, -1):
            ans[idx] *= suffix
            suffix *= nums[idx]

        return ans
