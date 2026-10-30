class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        ans = 0
        L = max(lights)

        for x in arrivalTime:
            r = x % period

            if r >= L:
                ans = max(ans, period - r)

        return ans
