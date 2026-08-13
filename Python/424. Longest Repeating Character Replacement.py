class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0
        max_length = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            while (right - left + 1) - max_count > k:
                old = s[left]
                count[old] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
