from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        results = []

        for idx, num in enumerate(nums):
            if dq and dq[0] <= idx - k:
                dq.popleft()

            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(idx)

            if idx >= k - 1:
                results.append(nums[dq[0]])

        return results
