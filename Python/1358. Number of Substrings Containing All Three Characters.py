class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        left = 0
        seen = {}

        for right, c in enumerate(s):
            seen[c] = seen.get(c, 0) + 1

            while len(seen) == 3:
                seen[s[left]] -= 1

                if seen[s[left]] == 0:
                    seen.pop(s[left])

                left += 1
                ans += n - right

        return ans
