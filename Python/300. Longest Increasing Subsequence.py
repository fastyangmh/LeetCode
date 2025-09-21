from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # method1
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue

                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

        # # method2
        # import bisect

        # sub = []

        # for n in nums:
        #     if not sub or sub[-1] < n:
        #         sub.append(n)
        #     else:
        #         idx = bisect.bisect_left(sub, n)
        #         sub[idx] = n

        # return len(sub)
