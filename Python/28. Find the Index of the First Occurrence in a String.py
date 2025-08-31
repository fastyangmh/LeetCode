class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for idx in range(len(haystack)):
            if haystack[idx : idx + len(needle)] == needle:
                return idx

        return -1
