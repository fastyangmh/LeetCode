class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            j = i % n
            x = nums[j]

            while stack and x > nums[stack[-1]]:
                ans[stack.pop()] = x

            if i < n:
                stack.append(i)

        return ans
