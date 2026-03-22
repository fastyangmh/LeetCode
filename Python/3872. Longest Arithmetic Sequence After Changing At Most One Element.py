class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        N = len(nums)

        left = [1] + [2] * (N - 1)

        for i in range(2, N):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                left[i] = left[i - 1] + 1

        right = [2] * (N - 1) + [1]

        for i in range(N - 3, -1, -1):
            if nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i]:
                right[i] = right[i + 1] + 1

        res = max(max(left), max(right)) + 1

        for i in range(1, N - 1):
            if ((nums[i + 1] - nums[i - 1]) % 2) == 0:
                diff = (nums[i + 1] - nums[i - 1]) // 2
                l = r = 1

                if i - 2 >= 0 and diff == nums[i - 1] - nums[i - 2]:
                    l = left[i - 1]
                if i + 2 < N and diff == nums[i + 2] - nums[i + 1]:
                    r = right[i + 1]

                res = max(res, l + r + 1)

        return min(N, res)
