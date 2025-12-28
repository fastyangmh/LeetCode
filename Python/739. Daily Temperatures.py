from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        rets = [0] * n

        for curr in range(n):
            if stack:
                curr_temp = temperatures[curr]

                while stack and curr_temp > temperatures[stack[-1]]:
                    prev = stack.pop()
                    rets[prev] = curr - prev

            stack.append(curr)

        return rets
