class Solution:
    def climbStairs(self, n: int) -> int:
        # # method1
        # map_ = [0] * (n + 1)
        # map_[0] = 1
        # map_[1] = 1

        # def helper(n):
        #     if map_[n] == 0:
        #         map_[n] = helper(n - 1) + helper(n - 2)
        #         return map_[n]
        #     return map_[n]

        # return helper(n)

        # # method2
        # map_ = [0] * (n + 1)
        # map_[0] = 1
        # map_[1] = 1

        # for idx in range(2, n + 1):
        #     map_[idx] = map_[idx - 1] + map_[idx - 2]

        # return map_[-1]

        # method3
        prev, curr = 1, 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr
