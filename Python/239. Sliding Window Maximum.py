from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for idx in range(len(nums)):
            if dq and dq[0] <= idx - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[idx]:
                dq.pop()

            dq.append(idx)

            if idx >= k - 1:
                res.append(nums[dq[0]])

        return res
