from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]

        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = float("inf")

        dq = deque()

        for i in range(len(prefix)):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return ans if ans != float("inf") else -1
