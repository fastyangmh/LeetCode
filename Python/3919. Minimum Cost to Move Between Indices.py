class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        right = [0] * (n - 1)
        left = [0] * n

        # cost: i -> i+1
        for i in range(n - 1):
            d = nums[i + 1] - nums[i]

            left_diff = nums[i] - nums[i - 1] if i > 0 else float('inf')
            right_diff = d

            if right_diff < left_diff:
                right[i] = 1
            else:
                right[i] = d

        # cost: i -> i-1
        for i in range(1, n):
            d = nums[i] - nums[i - 1]

            left_diff = d
            right_diff = nums[i + 1] - nums[i] if i < n - 1 else float('inf')

            if left_diff <= right_diff:
                left[i] = 1
            else:
                left[i] = d

        # prefix for right
        preR = [0] * n
        for i in range(n - 1):
            preR[i + 1] = preR[i] + right[i]

        # prefix for left
        preL = [0] * n
        for i in range(1, n):
            preL[i] = preL[i - 1] + left[i]

        ans = []

        for l, r in queries:
            if l < r:
                ans.append(preR[r] - preR[l])
            else:
                ans.append(preL[l] - preL[r])

        return ans