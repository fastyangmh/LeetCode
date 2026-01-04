class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_len = max_freq = 0
        counter = {}

        for right, ch in enumerate(s):
            counter[ch] = counter.get(ch, 0) + 1

            max_freq = max(max_freq, counter[ch])

            while right - left + 1 - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
