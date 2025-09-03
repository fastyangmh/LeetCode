class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # method1
        # left = max_len = 0

        # for right in range(len(s)):
        #     while s[right] in s[left:right] and left < right:
        #         left += 1
        #     max_len = max(max_len, right - left + 1)

        # return max_len

        # method2
        left = max_len = 0
        seen = {}

        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            max_len = max(max_len, right - left + 1)
            seen[c] = right

        return max_len
