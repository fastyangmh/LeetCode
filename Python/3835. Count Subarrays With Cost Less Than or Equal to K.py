from collections import deque


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_deque = deque()
        min_deque = deque()
        count = 0
        left = 0

        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            while (nums[max_deque[0]] - nums[min_deque[0]]) * (right - left + 1) > k:
                if max_deque[0] == left:
                    max_deque.popleft()

                if min_deque[0] == left:
                    min_deque.popleft()

                left += 1

            count += right - left + 1

        return count
