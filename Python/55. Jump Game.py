class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # method1
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for idx in range(len(nums) - 1):
        #     if idx != 0:
        #         dp[idx] = max(dp[idx - 1] - 1, nums[idx])

        #     if dp[idx] == 0:
        #         return False

        # return True

        # method2
        max_reach = 0

        for idx, jump in enumerate(nums):
            if max_reach < idx:
                return False

            max_reach = max(max_reach, idx + jump)

            if max_reach >= len(nums) - 1:
                return True

        return True
