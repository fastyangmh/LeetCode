class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = 0
        max_gain = 0
        i = 0
        prev_zeros = float("-inf")

        while i < n:
            j = i + 1

            while j < n and s[j] == s[i]:
                j += 1

            curr = j - i

            if s[i] == "1":
                ans += curr
            else:
                max_gain = max(max_gain, prev_zeros + curr)
                prev_zeros = curr

            i = j

        return ans + max_gain
