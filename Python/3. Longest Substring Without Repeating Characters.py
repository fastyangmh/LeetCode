class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        l = 0

        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1

            ans = max(ans, r - l + 1)
            seen[c] = r

        return ans
