from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}
        start = left = right = valid = 0
        min_len = float("inf")

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1

                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < min_len:
                    min_len = right - left
                    start = left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_len == float("inf") else s[start : start + min_len]
