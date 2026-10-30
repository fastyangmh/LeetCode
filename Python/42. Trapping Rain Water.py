class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0

        while l < r:
            hl, hr = height[l], height[r]

            if hl < hr:
                l += 1

                if hl > left_max:
                    left_max = hl
                else:
                    ans += left_max - hl

            else:
                r -= 1

                if hr > right_max:
                    right_max = hr
                else:
                    ans += right_max - hr

        return ans
