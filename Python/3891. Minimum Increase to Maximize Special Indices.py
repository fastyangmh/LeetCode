class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        # prev not taken
        dp0 = 0
        cost0 = 0

        # prev taken
        dp1 = -(10**9)
        cost1 = 10**9

        for i in range(1, len(nums) - 1):
            need = max(nums[i - 1], nums[i + 1]) + 1
            curr_cost = max(0, need - nums[i])

            # not take curr
            if dp0 > dp1:
                ndp0 = dp0
                ncost0 = cost0
            elif dp1 > dp0:
                ndp0 = dp1
                ncost0 = cost1
            else:
                ndp0 = dp0
                ncost0 = min(cost0, cost1)

            # take curr
            ndp1 = dp0 + 1
            ncost1 = cost0 + curr_cost

            # update
            dp0, cost0 = ndp0, ncost0
            dp1, cost1 = ndp1, ncost1

        if dp0 > dp1:
            return cost0
        if dp1 > dp0:
            return cost1

        return min(cost0, cost1)
