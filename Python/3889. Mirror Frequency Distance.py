class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = [0] * (ord("z") + 1)

        for c in s:
            freq[ord(c)] += 1

        ans = 0

        for c in s:
            ci = ord(c)

            if freq[ci] == 0:
                continue

            if c.isdigit():
                mi = ord("0") + ord("9") - ci
            else:
                mi = ord("a") + ord("z") - ci

            ans += abs(freq[ci] - freq[mi])

            freq[ci] = 0
            freq[mi] = 0

        return ans
