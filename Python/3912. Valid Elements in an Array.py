class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = float("-inf")

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i + 1])

        ans = []
        left_max = float("-inf")

        for i, num in enumerate(nums):
            if i == 0 or i == n - 1 or num > left_max or num > right_max[i]:
                ans.append(num)

            left_max = max(left_max, num)

        return ans
