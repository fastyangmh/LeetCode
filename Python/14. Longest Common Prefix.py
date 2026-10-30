class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]

            k = min(len(prefix), len(s))
            j = 0

            while j < k and s[j] == prefix[j]:
                j += 1

            prefix = prefix[:j]

            if not prefix:
                return ""

        return prefix
