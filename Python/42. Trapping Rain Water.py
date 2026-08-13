class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0

        while left < right:
            hl, hr = height[left], height[right]

            if hl < hr:
                left += 1

                if hl > left_max:
                    left_max = hl
                else:
                    ans += left_max - hl
            else:
                right -= 1

                if hr > right_max:
                    right_max = hr
                else:
                    ans += right_max - hr

        return ans
