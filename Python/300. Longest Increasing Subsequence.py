from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # method1
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

        # # method2
        # tails = []

        # for num in nums:
        #     idx = bisect_left(tails, num)

        #     if idx == len(tails):
        #         tails.append(num)
        #     else:
        #         tails[idx] = num

        # return len(tails)
