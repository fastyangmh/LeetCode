class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        ans = []
        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] != 0:
                    continue

                if dp[j] + 1 <= dp[i]:
                    continue

                dp[i] = dp[j] + 1
                parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        while max_idx != -1:
            ans.append(nums[max_idx])
            max_idx = parent[max_idx]

        return ans
