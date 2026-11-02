class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            hl, hr = height[l], height[r]
            h = min(hl, hr)
            w = r - l
            ans = max(ans, h * w)

            if hl < hr:
                l += 1
            else:
                r -= 1

        return ans
