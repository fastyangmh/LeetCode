from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        window_sum = 0
        ans = 0

        for right in range(len(nums)):
            x = nums[right]
            freq[x] += 1
            window_sum += x

            if right - left + 1 > k:
                y = nums[left]
                freq[y] -= 1

                if freq[y] == 0:
                    del freq[y]

                window_sum -= y
                left += 1

            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, window_sum)

        return ans
